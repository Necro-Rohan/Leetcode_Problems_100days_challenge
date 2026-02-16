# Write your MySQL query statement below
SELECT
  s.score,
  (
    SELECT COUNT(DISTINCT ss.score) + 1
    FROM Scores ss
    WHERE ss.score > s.score
  ) AS `rank`
FROM Scores s
ORDER BY s.score DESC;