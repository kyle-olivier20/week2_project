CREATE TABLE cityname (  
    geonameid INT(7) UNSIGNED default NULL,
    name VARCHAR(255) default NULL,
    population INT(10) UNSIGNED default NULL,
    PRIMARY KEY (geonameid)
) AUTO_INCREMENT=1;