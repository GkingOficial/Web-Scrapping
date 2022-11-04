
<h1 align="center">
  Web Scrapping da Tabela FIPE
</h1>

<p align="center">
 <a href="#objetivo">Objetivo</a> •
 <a href="#requisitos">Requisitos</a> • 
 <a href="#passo-a-passo">Passo-a-passo</a> • 
 <a href="#autor">Autor</a>
</p>

### Objetivo

<p>

</p>

### Requisitos

Para rodar esta aplicação, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python + pip](https://www.python.org/downloads/) e [virtualenv](https://virtualenv.pypa.io/en/latest/).

### Passo-a-passo

```bash
# Clone este repositório
$ git clone https://github.com/GkingOficial/Web-Scrapping

# Acesse a pasta do projeto no terminal/cmd
$ cd Web-Scrapping

# Crie um ambiente virtual para instalar as dependências
$ virtualenv myENV

# Entre no ambiente virtual
$ source myENV/bin/activate

# Instale as dependências
$ pip3 install -r requirements.txt

```

### Execução

É interessante que você abra em seu editor de texto os seguintes arquivos:
- vehicles_to_search.json
- indices_de_busca.json
- vehicles_with_price.json

O primeiro arquivo contém a lista de modelos que serão buscados na Tabela Fipe.

O segundo arquivo contém os indices que referenciam algum modelo específico do primeiro arquivo. Esses índices informam o modelo especifico que o web scrapping deverá buscar na Tabela Fipe, e por isso, são atualizados a medida que a busca estiver acontecendo na página.

O terceiro arquivo contém os modelos pesquisados na tabela Fipe com o seu respectivo preço. Também é um arquivo que deve ser atualizado a medida que a busca estiver rodando.

```bash
# Execute a aplicação
$ python3 3-web_scrapping.py
```

Você pode acompanhar a busca sendo feita pelo terminal da própria execução.

### Autor

<img 
    style="border-radius: 50%;"
    src="https://avatars2.githubusercontent.com/u/51214434?s=400&u=439cd150f8dbf2706452ce6a362992e077285793&v=4"
    width="100px;"
    alt="Daniel Alencar"
/>

[![Instagram Badge](https://img.shields.io/badge/-@daniel_alencar_-de2099?style=flat-square&logo=Instagram&logoColor=white&link=https://www.linkedin.com/in/Daniel746/)](https://www.instagram.com/daniel_alencar_/) [![Linkedin Badge](https://img.shields.io/badge/-Daniel-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/Daniel746/)](https://www.linkedin.com/in/Daniel746/) [![Gmail Badge](https://img.shields.io/badge/-danielalencar746@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:danielalencar746@gmail.com)](mailto:danielalencar746@gmail.com)

<img 
    style="border-radius: 50%;"
    src="https://avatars2.githubusercontent.com/u/51214434?s=400&u=439cd150f8dbf2706452ce6a362992e077285793&v=4"
    width="100px;"
    alt="Daniel Alencar"
/>

[![Instagram Badge](https://img.shields.io/badge/-@daniel_alencar_-de2099?style=flat-square&logo=Instagram&logoColor=white&link=https://www.linkedin.com/in/Daniel746/)](https://www.instagram.com/daniel_alencar_/) [![Linkedin Badge](https://img.shields.io/badge/-Daniel-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/Daniel746/)](https://www.linkedin.com/in/Daniel746/) [![Gmail Badge](https://img.shields.io/badge/-danielalencar746@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:danielalencar746@gmail.com)](mailto:danielalencar746@gmail.com)