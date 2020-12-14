CREATE TABLE IF NOT EXISTS "dbmigration" (
	"version" INTEGER NOT NULL,
	"executed_on" TIMESTAMP NULL,
	PRIMARY KEY ("version")
);
