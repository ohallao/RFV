# Projeto RFV - Segmentação de Clientes

Este projeto utiliza a metodologia RFV (Recência, Frequência e Valor) para segmentar clientes com base em seus comportamentos de compra. A aplicação foi desenvolvida em Python, utilizando bibliotecas como Streamlit para a interface de usuário, pandas para manipulação de dados, e métodos de clusterização para agrupar clientes de forma eficiente.

# Estrutura dos Arquivos
1. app_RFV.py
Este arquivo contém a lógica da aplicação para calcular os componentes RFV e segmentar os clientes. Ele inclui as seguintes funcionalidades:

Cálculo de Recência (R): Dias desde a última compra de cada cliente.
Cálculo de Frequência (F): Número de compras realizadas no período determinado.
Cálculo de Valor (V): Total gasto pelo cliente em suas compras.
Exportação de Dados: Funções que permitem exportar os dados gerados para arquivos CSV e Excel.
Interface Gráfica com Streamlit: Utiliza o Streamlit para criar uma interface interativa, onde os resultados da segmentação podem ser visualizados e analisados.

2. app_Projeto.py
Este arquivo está focado na aplicação de técnicas de clusterização para a segmentação de clientes com base no cálculo de distâncias e hierarquia. Entre as funcionalidades, temos:

Clusterização Hierárquica: Implementa a técnica de clusterização aglomerativa para agrupar clientes com perfis semelhantes.
Pré-processamento dos Dados: Inclui etapas de normalização dos dados utilizando StandardScaler.
Visualização dos Clusters: Gera dendogramas para representar visualmente os agrupamentos realizados.
Interface Gráfica com Streamlit: Assim como o app_RFV.py, este arquivo também utiliza o Streamlit para uma interface interativa que permite a visualização dos resultados da análise de clusterização.

# Como Executar no Render
A aplicação está disponível no Render. Para executar o projeto no Render, siga os seguintes passos:

Deploy no Render: Você pode criar um deploy diretamente no Render utilizando este repositório. Caso ainda não tenha uma conta no Render, crie uma e siga as instruções para conectar o seu repositório do GitHub com a plataforma.

Configuração no Render: Defina os seguintes parâmetros na configuração do serviço no Render:

Build Command: pip install -r requirements.txt
Start Command: streamlit run app_RFV.py ou streamlit run app_Projeto.py, dependendo do arquivo que deseja rodar.
Acesso: Após o deploy, você poderá acessar a aplicação através do link gerado pelo Render, que estará disponível diretamente no painel de controle da plataforma.

# Dependências
- pandas
- numpy
- streamlit
- matplotlib
- scikit-learn
- xlsxwriter
- gower

# Objetivos do Projeto
O objetivo deste projeto é utilizar a técnica RFV para segmentação de clientes, permitindo que empresas personalizem suas campanhas de marketing e estratégias de retenção. A aplicação de métodos de clusterização hierárquica ajuda a identificar padrões de comportamento semelhantes entre os clientes, gerando insights valiosos.
