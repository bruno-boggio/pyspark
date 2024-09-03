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


-- Desafio:
-- Tabela: Clientes
-- Colunas: id, nome, cidade, compra_total
-- Objetivo: Encontre os clientes que têm um compra_total acima da média das compras totais dos clientes na sua própria cidade.

SELECT id, nome, cidade 
FROM clientes 
WHERE compra_total > (
    SELECT AVG(compra_total)
    FROM clientes c2
    WHERE c2.cidade = clientes.cidade
);


-- Desafio:
-- Tabela: Vendas
-- Colunas: id, vendedor, valor
-- Objetivo: Encontre os vendedores que realizaram vendas com um valor acima da média das vendas feitas por todos os vendedores.

SELECT id, vendedor 
FROM vendas 
WHERE valor > (SELECT AVG(valor) FROM vendas);
