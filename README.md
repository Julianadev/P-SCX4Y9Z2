# Projeto de Busca de CEP

Este projeto usa Selenium e Python para buscar informações de CEPs automaticamente.

## Dependências

O projeto depende das seguintes bibliotecas Python:

- Selenium
- pandas

## Como usar

1. Certifique-se de que todas as dependências estão instaladas.
2. Execute o script Python principal.

O script irá ler os CEPs de um arquivo Excel, buscar as informações correspondentes no site dos Correios e salvar os resultados de volta no arquivo Excel.

## Detalhes do Script

O script contém várias funções:

- `buscar_cep()`: Esta função busca as informações de um CEP no site dos Correios.
- `main()`: Esta é a função principal que lê os CEPs do arquivo Excel, chama a função `buscar_cep()` para cada CEP e salva os resultados.

## Contribuindo

Contribuições para este projeto são bem-vindas. Por favor, abra uma issue ou um pull request se você quiser contribuir.

## Licença

Este projeto é licenciado sob os termos da licença MIT.
