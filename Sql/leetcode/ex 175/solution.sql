SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P LEFT JOIN Address A
on P.personId = A.personId

--https://leetcode.com/problems/combine-two-tables/