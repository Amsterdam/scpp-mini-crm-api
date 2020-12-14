CREATE OR REPLACE FUNCTION dbmigration_1() RETURNS bool AS $$
DECLARE
	executed_on TIMESTAMP;
BEGIN
	SELECT dbmigration.executed_on INTO executed_on FROM dbmigration WHERE dbmigration.version = 1;

	IF executed_on IS NOT NULL THEN
		RETURN FALSE;
	END IF;

    DROP TABLE IF EXISTS public.contacts CASCADE;

    DROP SEQUENCE IF EXISTS public.contacts_id_seq;

    DROP TABLE IF EXISTS public.enhanced_note_contact CASCADE;

    DROP TABLE IF EXISTS public.enhanced_note_school CASCADE;

    DROP TABLE IF EXISTS public.enhanced_note_tag CASCADE;

    DROP TABLE IF EXISTS public.enhanced_notes CASCADE;

    DROP SEQUENCE IF EXISTS public.enhanced_notes_id_seq;

    DROP TABLE IF EXISTS public.notes CASCADE;

    DROP SEQUENCE IF EXISTS public.notes_id_seq;

    DROP TABLE IF EXISTS public.schools CASCADE;

    DROP SEQUENCE IF EXISTS public.schools_id_seq;

    DROP TABLE IF EXISTS public.tags CASCADE;

    DROP SEQUENCE IF EXISTS public.tags_id_seq;


	INSERT INTO dbmigration ("version", "executed_on") VALUES (1, CURRENT_TIMESTAMP);
	RETURN TRUE;
END;
$$ LANGUAGE plpgsql;

SELECT dbmigration_1();