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
## Links:
- [Testing Python AWS applications using LocalStack](https://hands-on.cloud/testing-python-aws-applications-using-localstack/#h-working-with-lambda-in-python-using-localstack-boto3)
- [https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html)
