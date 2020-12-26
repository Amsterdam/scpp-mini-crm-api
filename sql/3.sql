CREATE OR REPLACE FUNCTION dbmigration_3() RETURNS bool AS $$
DECLARE
	executed_on TIMESTAMP;
BEGIN
	SELECT dbmigration.executed_on INTO executed_on FROM dbmigration WHERE dbmigration.version = 3;

	IF executed_on IS NOT NULL THEN
		RETURN FALSE;
	END IF;
    ALTER TABLE public.contacts ADD COLUMN reference character varying;
    --- truncate tag and related tables assume we don't have production data yet
    TRUNCATE TABLE public.tags CASCADE;
    ALTER SEQUENCE public.tags_id_seq RESTART WITH 1000;
    --- start values
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (1,'parkeervergunning','default','Parkeervergunning (PVG)','2020-10-05 13:01:51.712308+00',NULL);
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (2,'wonen','default','Wonen (W)','2020-10-05 13:01:51.712308+00',NULL);
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (11,'reiskostenvergoeding','default','Reiskostenvergoeding (RKV)','2020-11-19 10:57:14.488303+00',NULL);
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (12,'administratie','default','Administratie (A)','2020-11-19 10:57:14.491097+00',NULL);
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (13,'bestuur','default','Bestuur (B)','2020-11-19 10:57:14.493309+00',NULL);
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (14,'directie','default','Directie (D)','2020-11-19 10:57:14.495369+00',NULL);
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (15,'leraren','default','Leraren (L)','2020-11-19 10:57:14.497452+00',NULL);
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (16,'vraag','default','Vraag','2020-11-19 10:57:14.497452+00',NULL);
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (17,'klacht','default','Klacht','2020-11-19 10:57:14.497452+00',NULL);
    INSERT INTO public.tags(id, tag, type, description, created_at, updated_at) VALUES (18,'melding','default','Melding','2020-11-19 10:57:14.497452+00',NULL);


	INSERT INTO dbmigration ("version", "executed_on") VALUES (3, CURRENT_TIMESTAMP);
	RETURN TRUE;
END;
$$ LANGUAGE plpgsql;

SELECT dbmigration_3();