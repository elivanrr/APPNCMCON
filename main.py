#Anotações requisitos para desenvolvimento da aplicação:
# 1- Pois desde  1/1/2016, com a Nota Técnica 2015/002, foi incluída uma nova regra de validação para autorização
# da NF-e, que verifica se a NCM informada existe na tabela publicada pelo Ministério do
# Desenvolvimento, Indústria e Comércio Exterior (MDIC) ou TIPI ou na TEC
#Em resumo, para identificarmos corretamente a NCM de um produto precisamos conhecer:
#1º -As seis regras do Sistema Harmonizado
#2º - As 21 Notas de Secções
#3º - As 97 Notas de Capítulos
#4º - As mais de 1.200 Notas de Posição NESH
#Importante: O trabalho não termina com a classificação do produto. Você deve monitorar possíveis
#alterações da NCM, das quais as mais comuns são: desmembramentos, extinção ou mesmo criação
#de novos códigos.
#Considerar  que para conformidade ainda tem o processo e as formas de tributação