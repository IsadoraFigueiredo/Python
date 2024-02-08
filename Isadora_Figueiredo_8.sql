/*1*/
SELECT
    jogadores.pretty_name,
    aparicoes.competition_id
FROM 
    jogadores
INNER JOIN
    aparicoes
ON jogadores.player_id = aparicoes.player_id    

/*2*/
SELECT
    jogadores.pretty_name,
    aparicoes.player_club_id
FROM 
    jogadores
LEFT JOIN
    aparicoes
ON 
	jogadores.player_id = aparicoes.player_id  

/*3*/
SELECT
    jogos_tratados.referee,
    SUM (aparicoes.red_cards) AS qt_red_cards
FROM 
	jogos_tratados
LEFT JOIN 
	aparicoes ON jogos_tratados.game_id = aparicoes.game_id
GROUP BY
	referee

/*4*/
SELECT
    jogadores.pretty_name,
    aparicoes.player_club_id
FROM 
    jogadores
RIGHT JOIN
    aparicoes
ON 
	jogadores.player_id = aparicoes.player_id  

/*5*/
SELECT
    jogadores.pretty_name,
    aparicoes.player_club_id
FROM 
    jogadores
FULL OUTER JOIN
    aparicoes
ON 
	jogadores.player_id = aparicoes.player_id 

/*6*/
SELECT
    jogadores.pretty_name,
    SUM (aparicoes.goals) AS qt_goals
FROM
	jogadores
LEFT JOIN
	aparicoes ON aparicoes.player_id = jogadores.player_id
GROUP BY
	jogadores.pretty_name
HAVING
	SUM (aparicoes.goals) > 0 AND SUM (aparicoes.goals) IS NOT NULL