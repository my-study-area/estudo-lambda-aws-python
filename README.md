# estudo-lambda-aws-python

## Começando
```
docker-compose up -d
# Para acessar o dashboard do localstack acesse: https://app.localstack.cloud./

# instala as dependências
pip install -r requirements.txt

# executa os testes
pytest -s .

# lista as functions criadas
aws --endpoint-url=http://localhost:4566 lambda list-functions --max-items 10
```

## Anotações
Criando executando um lambda com AWS CLI:
```bash
# cria role para lambda
aws --endpoint-url=http://localhost:4566 iam create-role \
--role-name lambda-ex --assume-role-policy-document \
'{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": \
{"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

# lista as roles criadas
aws --endpoint-url=http://localhost:4566 iam list-roles

# adiciona permissão de execução na role lambda-ex
aws --endpoint-url=http://localhost:4566 iam attach-role-policy \
--role-name lambda-ex \
--policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# lista as polices anexadas na role lambda-ex
aws --endpoint-url=http://localhost:4566 iam list-attached-role-policies \
--role-name lambda-ex

# cria a lambda
aws --endpoint-url=http://localhost:4566 \
lambda create-function --function-name my-lambda-function \
--zip-file fileb://lambda-ex.zip \
--handler lambda.handler --runtime python3.8 \
--role arn:aws:iam::000000000000:role/lambda-ex 

# executando a lambda
aws --endpoint-url=http://localhost:4566 \
lambda invoke --function-name my-lambda-function \
out --log-type- Tail --query 'LogResult' --output text

# adiciona evento
aws --endpoint-url=http://localhost:4566 events put-rule \
--name my-scheduled-rule \
--schedule-expression 'rate(2 minutes)'

# adiciona perissão da schedule na lambda
aws --endpoint-url=http://localhost:4566 lambda add-permission \
--function-name my-lambda-function \
--statement-id my-scheduled-event \
--action 'lambda:InvokeFunction' \
--principal events.amazonaws.com \
--source-arn arn:aws:events:us-east-1:000000000000:rule/my-scheduled-rule

# adiciona target no evento
aws --endpoint-url=http://localhost:4566 events \
put-targets --rule my-scheduled-rule \
--targets file://targets.json
```
## Links:
- [Testing Python AWS applications using LocalStack](https://hands-on.cloud/testing-python-aws-applications-using-localstack/#h-working-with-lambda-in-python-using-localstack-boto3)
- [https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html)
