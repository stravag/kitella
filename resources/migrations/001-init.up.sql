CREATE EXTENSION pgcrypto;
--;;
CREATE TABLE players (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    firstname   TEXT NOT NULL,
    lastname    TEXT NOT NULL,
    email       TEXT NOT NULL
);
--;;
CREATE TABLE events (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        TEXT NOT NULL,
    description TEXT
)
--;;
CREATE TABLE events_players (
    events_id   UUID REFERENCES events (id),
    players_id  UUID REFERENCES players (id),
    PRIMARY KEY (events_id, players_id)
)
--;;
CREATE TABLE players_classifications (
    classified_player_id    UUID REFERENCES players (id),
    classifying_player_id   UUID REFERENCES players (id),
    events_id               UUID REFERENCES events (id),
    val                     DECIMAL NOT NULL,
    PRIMARY KEY (classified_player_id, classifying_player_id, events_id)
)