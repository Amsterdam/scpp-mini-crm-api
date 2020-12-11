--
-- PostgreSQL database dump
--
-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4
SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;


CREATE TABLE public.contacts (
    id integer NOT NULL,
    naam character varying,
    email character varying,
    phone character varying,
    school_id integer,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone
);
ALTER TABLE public.contacts;

CREATE SEQUENCE public.contacts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE public.contacts_id_seq;

ALTER SEQUENCE public.contacts_id_seq OWNED BY public.contacts.id;

CREATE TABLE public.enhanced_note_contact (
    contact_id integer,
    enhanced_note_id integer
);

ALTER TABLE public.enhanced_note_contact;

CREATE TABLE public.enhanced_note_school (
    school_id integer,
    enhanced_note_id integer
);

ALTER TABLE public.enhanced_note_school;

CREATE TABLE public.enhanced_note_tag (
    tag_id integer,
    enhanced_note_id integer
);

ALTER TABLE public.enhanced_note_tag;

CREATE TABLE public.enhanced_notes (
    id integer NOT NULL,
    contact_id integer,
    note character varying,
    start timestamp with time zone DEFAULT now(),
    "end" timestamp with time zone DEFAULT now(),
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone
);
ALTER TABLE public.enhanced_notes;

CREATE SEQUENCE public.enhanced_notes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.enhanced_notes_id_seq;

ALTER SEQUENCE public.enhanced_notes_id_seq OWNED BY public.enhanced_notes.id;

CREATE TABLE public.notes (
    id integer NOT NULL,
    note character varying,
    contact_id integer,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone
);

ALTER TABLE public.notes;

CREATE SEQUENCE public.notes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE public.notes_id_seq;

ALTER SEQUENCE public.notes_id_seq OWNED BY public.notes.id;

CREATE TABLE public.schools (
    id integer NOT NULL,
    school_id integer,
    lrkp_id character varying,
    school_type character varying,
    brin character varying,
    vestigingsnummer character varying,
    naam character varying,
    grondslag character varying,
    schoolwijzer_url character varying,
    onderwijsconcept character varying,
    heeft_voorschool boolean,
    leerlingen integer,
    address character varying,
    postcode character varying,
    suburb character varying,
    website character varying,
    email character varying,
    phone character varying,
    city character varying,
    point public.geometry(Point,4326)
);

ALTER TABLE public.schools;

CREATE SEQUENCE public.schools_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.schools_id_seq;

ALTER SEQUENCE public.schools_id_seq OWNED BY public.schools.id;

CREATE TABLE public.tags (
    id integer NOT NULL,
    tag character varying,
    type character varying,
    description character varying,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone
);

ALTER TABLE public.tags;

CREATE SEQUENCE public.tags_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.tags_id_seq;

ALTER SEQUENCE public.tags_id_seq OWNED BY public.tags.id;

ALTER TABLE ONLY public.contacts ALTER COLUMN id SET DEFAULT nextval('public.contacts_id_seq'::regclass);

ALTER TABLE ONLY public.enhanced_notes ALTER COLUMN id SET DEFAULT nextval('public.enhanced_notes_id_seq'::regclass);

ALTER TABLE ONLY public.notes ALTER COLUMN id SET DEFAULT nextval('public.notes_id_seq'::regclass);

ALTER TABLE ONLY public.schools ALTER COLUMN id SET DEFAULT nextval('public.schools_id_seq'::regclass);

ALTER TABLE ONLY public.tags ALTER COLUMN id SET DEFAULT nextval('public.tags_id_seq'::regclass);

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.enhanced_notes
    ADD CONSTRAINT enhanced_notes_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.schools
    ADD CONSTRAINT schools_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_tag_key UNIQUE (tag);

CREATE INDEX idx_schools_point ON public.schools USING gist (point);

CREATE INDEX ix_contacts_id ON public.contacts USING btree (id);

CREATE UNIQUE INDEX ix_contacts_naam ON public.contacts USING btree (naam);

CREATE INDEX ix_enhanced_notes_id ON public.enhanced_notes USING btree (id);

CREATE INDEX ix_notes_id ON public.notes USING btree (id);

CREATE INDEX ix_schools_id ON public.schools USING btree (id);

CREATE INDEX ix_schools_naam ON public.schools USING btree (naam);

CREATE INDEX ix_tags_id ON public.tags USING btree (id);

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_school_id_fkey FOREIGN KEY (school_id) REFERENCES public.schools(id);

ALTER TABLE ONLY public.enhanced_note_contact
    ADD CONSTRAINT enhanced_note_contact_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES public.contacts(id);

ALTER TABLE ONLY public.enhanced_note_school
    ADD CONSTRAINT enhanced_note_school_school_id_fkey FOREIGN KEY (school_id) REFERENCES public.schools(id);

ALTER TABLE ONLY public.enhanced_notes
    ADD CONSTRAINT enhanced_notes_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES public.contacts(id);

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES public.contacts(id);
