# DROP TABLES

songplay_table_drop = """drop table if exists songplay;"""
user_table_drop = """drop table if exists "user";"""
song_table_drop = """drop table if exists song;"""
artist_table_drop = """drop table if exists artist;"""
time_table_drop = """drop table if exists "time";"""

# CREATE TABLES

songplay_table_create = ("""
    create table if not exists songplay (
        songplay_id serial
        , start_time timestamp 
        , user_id integer not null
        , level varchar
        , song_id varchar
        , artist_id varchar
        , session_id integer
        , location varchar
        , user_agent varchar
    )
""")

user_table_create = ("""
    create table if not exists "user" (
        user_id integer not null
        , first_name varchar
        , last_name varchar
        , gender varchar
        , level varchar
    )
""")

song_table_create = ("""
    create table if not exists song (
        song_id varchar not null
        , title varchar not null
        , artist_id varchar not null
        , year integer
        , duration float
    )
""")

artist_table_create = ("""
    create table if not exists artist (
        artist_id varchar not null
        , name varchar not null
        , location varchar
        , latitude float
        , longitude float
    )
""")

time_table_create = ("""
    create table if not exists "time" (
        start_time timestamp
        , hour integer
        , day varchar
        , week integer
        , month integer
        , year integer
        , weekday varchar
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    insert into songplay (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    values (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    insert into "user" (user_id, first_name, last_name, gender, level)
    values (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
    insert into song (song_id, title, artist_id, year, duration)
    values (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
    insert into artist (artist_id, name, location, latitude, longitude)
    values (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
    insert into "time" (start_time, hour, day, week, month, year, weekday)
    values (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
    select song.song_id, song.artist_id
    from song
    join artist on artist.artist_id=song.artist_id
    where song.title ilike %s and artist.name ilike %s and song.duration=%s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]