-- ЗАДАНИЕ 2
-- Самый длинный трек
SELECT
    t1.id_album,
    t1.duration
FROM
    tracks as t1
WHERE
    t1.duration = (
        SELECT
            MAX(duration)
        FROM
            tracks
    );

-- Треки, длинее 3,5 минут
SELECT
    t1.title
FROM
    tracks as t1
WHERE
    t1.duration >= '00:03:30';

-- сборники, вышедшие в период с 2018 по 2020 год
SELECT
    t1.title
FROM
    songbooks as t1
WHERE
    t1.year between 2018 AND 2020;

-- Исполнители, чьё имя состоит из одного слова
SELECT
    t1.name
FROM
    artists as t1
WHERE
    string_agg(t1.name, ' ') = t1.name;

-- Название треков, которые содержат слово "мой" или "my"
SELECT
    t1.title
FROM
    tracks as t1
WHERE
    title LIKE '%мой%'
    OR title LIKE '%my%';

-- ЗАДАНИЕ 3
-- Количество исполнителей в каждом жанре
SELECT
    g.name,
    count(*)
FROM
    genres g
    join artist_genres ag ON g.id = ag.id_genre
GROUP BY
    g.name;

-- Количество треков, вошедших в альбомы 2019–2020 годов
SELECT
    count(*)
FROM
    tracks t
    join albums a ON t.id_album = a.id
WHERE
    a.year >= 2019
    AND a.year <= 2020;

-- Средняя продолжительность треков по каждому альбому
SELECT
    a.id,
    avg(t.duration)
FROM
    albums a
    join tracks t ON a.id = t.id_album
GROUP BY
    a.id;

-- Все исполнители, которые не выпустили альбомы в 2020 году:
SELECT a.name
FROM artists a
WHERE a.id NOT IN
    (SELECT
        a.id
    FROM
       artists a
       left join artist_albums aa ON a.id = aa.id_artist
    WHERE
        aa.id_album is null
        AND YEAR(a.year) = 2020);

-- Названия сборников, в которых присутствует конкретный исполнитель:
SELECT
    sb.title
FROM
    songbooks sb
    join songbook_tracks st ON sb.id = st.songbook_id
    join tracks t ON st.track_id = t.id
    join artist_albums aa ON t.id_album = aa.id_album
    join artists a ON aa.id_artist = a.id
WHERE
    a.name = 'Имя исполнителя';
