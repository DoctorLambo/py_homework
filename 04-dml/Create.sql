CREATE TABLE IF NOT EXISTS "artist_genres" (
	"id_artist" serial NOT NULL,
	"id_genre" text NOT NULL,
	PRIMARY KEY ("id_artist", "id_genre")
);

CREATE TABLE IF NOT EXISTS "genres" (
	"id" int NOT NULL,
	"name" string NOT NULL,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "artist_albums" (
	"id_album" serial NOT NULL,
	"id_artist" serial NOT NULL,
	PRIMARY KEY ("id_album", "id_artist")
);

CREATE TABLE IF NOT EXISTS "artists" (
	"id" int NOT NULL,
	"name" string NOT NULL,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "albums" (
	"id" int NOT NULL,
	"title" string NOT NULL,
	"year" date NOT NULL,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "tracks" (
	"id" int NOT NULL,
	"id_album" serial NOT NULL,
	"duration" datetime NOT NULL,
	PRIMARY KEY ("id", "id_album")
);

CREATE TABLE IF NOT EXISTS "songbook" (
	"id" int NOT NULL,
	"title" string NOT NULL,
	"year" date NOT NULL,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "songbook_tracks" (
	"songbook_id" serial NOT NULL,
	"track_id" serial NOT NULL,
	PRIMARY KEY ("songbook_id", "track_id")
);

ALTER TABLE "artist_genres" ADD CONSTRAINT "artist_genres_fk0" FOREIGN KEY ("id_artist") REFERENCES "artists"("id");

ALTER TABLE "artist_genres" ADD CONSTRAINT "artist_genres_fk1" FOREIGN KEY ("id_genre") REFERENCES "genres"("id");

ALTER TABLE "artist_albums" ADD CONSTRAINT "artist_albums_fk0" FOREIGN KEY ("id_album") REFERENCES "albums"("id");

ALTER TABLE "artist_albums" ADD CONSTRAINT "artist_albums_fk1" FOREIGN KEY ("id_artist") REFERENCES "artists"("id");


ALTER TABLE "tracks" ADD CONSTRAINT "tracks_fk1" FOREIGN KEY ("id_album") REFERENCES "albums"("id");

ALTER TABLE "songbook_tracks" ADD CONSTRAINT "songbook_tracks_fk0" FOREIGN KEY ("songbook_id") REFERENCES "songbook"("id");

ALTER TABLE "songbook_tracks" ADD CONSTRAINT "songbook_tracks_fk1" FOREIGN KEY ("track_id") REFERENCES "tracks"("id");
