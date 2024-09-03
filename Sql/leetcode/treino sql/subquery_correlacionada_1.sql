-- praticando subqueries relacionadas com o chatgpt

-- Exercício:
-- Tabela: Livros
-- Colunas: id, titulo, preco
-- Objetivo: Encontre os livros que têm um preço abaixo do preço médio de todos os livros.

Minha solução:

Select id, titulo 
From livros
Where preco <= (
    Select avg(preco) 
    from livros
    ); 



-- Desafio:
-- Tabela: Produtos
-- Colunas: id, categoria, preco
-- Objetivo: Encontre os produtos que têm um preço superior ao preço médio dos produtos na sua própria categoria.

Select id, categoria 
from produtos
where preco > (
    Select avg(preco)
    From produtos p2 
    Where p2.categoria = produtos.categoria
    ); 
