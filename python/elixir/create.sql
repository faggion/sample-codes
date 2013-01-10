CREATE TABLE users1 (
    id INT(11) NOT NULL,
    name VARCHAR(64),
    profile TEXT,
    PRIMARY KEY (id)
);

insert into users1 (id, name, profile) values (1, 'name1', 'profile1');
insert into users1 (id, name, profile) values (2, 'name2', 'profile2');
insert into users1 (id, name, profile) values (3, 'name3', 'profile3');

CREATE TABLE users2 (
    id INT(11) NOT NULL,
    name VARCHAR(64),
    profile TEXT,
    PRIMARY KEY (id)
);

insert into users2 (id, name, profile) values (4, 'name4', 'profile4');
insert into users2 (id, name, profile) values (5, 'name5', 'profile5');
insert into users2 (id, name, profile) values (6, 'name6', 'profile6');
