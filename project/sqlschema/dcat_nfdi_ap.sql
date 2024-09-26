-- # Class: "NamedThing" Description: "A generic grouping for any identifiable entity"
--     * Slot: id Description: The unique identifier of a thing.
-- # Class: "Dataset" Description: "A collection of data, published or curated by a single agent, and available for access or download in one or more representations."
--     * Slot: id Description: The unique identifier of a Dataset.
--     * Slot: Catalog_id Description: Autocreated FK slot
--     * Slot: was_generated_by_id Description: The property to specify the Activity (process) that created a Dataset.
-- # Class: "Catalog" Description: "A curated collection of metadata about data resources."
--     * Slot: id Description: The unique identifier of a Catalog.
--     * Slot: was_generated_by_id Description: The property to specify the Activity (process) that created a Dataset.
-- # Class: "Activity" Description: "An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities."
--     * Slot: id Description: 
--     * Slot: type Description: The type of activity according to the permissible values defined in the ActivityType enum.
--     * Slot: has_part_id Description: An activity that is a part of an activity.
-- # Class: "ObjectOfInterest" Description: "Something that is being observed, studied, modified, influenced or consumed within an activity."
--     * Slot: type Description: The type of object according to the permissible values defined in the ObjectType enum.
--     * Slot: id Description: The unique identifier of a thing.
--     * Slot: Activity_id Description: Autocreated FK slot
-- # Class: "Tool" Description: "Something with a certain function used within an activity to achieve the overall goal of the activity."
--     * Slot: type Description: The type of tool according to the permissible values defined in the ToolType enum.
--     * Slot: has_part Description: A tool that is a part of a tool.
--     * Slot: id Description: The unique identifier of a thing.
--     * Slot: Activity_id Description: Autocreated FK slot
-- # Class: "NamedThing_name" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: name Description: The name of a thing.
-- # Class: "NamedThing_description" Description: ""
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of a thing.
-- # Class: "Dataset_name" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: name Description: The name of a dcat:Dataset.
-- # Class: "Dataset_description" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of a dcat:Dataset.
-- # Class: "Catalog_name" Description: ""
--     * Slot: Catalog_id Description: Autocreated FK slot
--     * Slot: name Description: The name of a dcat:Catalog.
-- # Class: "Catalog_description" Description: ""
--     * Slot: Catalog_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of a dcat:Catalog.
-- # Class: "ObjectOfInterest_name" Description: ""
--     * Slot: ObjectOfInterest_id Description: Autocreated FK slot
--     * Slot: name Description: The name of a thing.
-- # Class: "ObjectOfInterest_description" Description: ""
--     * Slot: ObjectOfInterest_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of a thing.
-- # Class: "Tool_name" Description: ""
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: name Description: The name of a thing.
-- # Class: "Tool_description" Description: ""
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of a thing.

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Activity" (
	id INTEGER NOT NULL, 
	type VARCHAR(13), 
	has_part_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part_id) REFERENCES "Activity" (id)
);
CREATE TABLE "Catalog" (
	id TEXT NOT NULL, 
	was_generated_by_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by_id) REFERENCES "Activity" (id)
);
CREATE TABLE "ObjectOfInterest" (
	type VARCHAR(4), 
	id TEXT NOT NULL, 
	"Activity_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id)
);
CREATE TABLE "Tool" (
	type VARCHAR(12), 
	has_part TEXT, 
	id TEXT NOT NULL, 
	"Activity_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_part) REFERENCES "Tool" (id), 
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id)
);
CREATE TABLE "NamedThing_name" (
	"NamedThing_id" TEXT, 
	name TEXT, 
	PRIMARY KEY ("NamedThing_id", name), 
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id)
);
CREATE TABLE "NamedThing_description" (
	"NamedThing_id" TEXT, 
	description TEXT, 
	PRIMARY KEY ("NamedThing_id", description), 
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id)
);
CREATE TABLE "Dataset" (
	id TEXT NOT NULL, 
	"Catalog_id" TEXT, 
	was_generated_by_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Catalog_id") REFERENCES "Catalog" (id), 
	FOREIGN KEY(was_generated_by_id) REFERENCES "Activity" (id)
);
CREATE TABLE "Catalog_name" (
	"Catalog_id" TEXT, 
	name TEXT NOT NULL, 
	PRIMARY KEY ("Catalog_id", name), 
	FOREIGN KEY("Catalog_id") REFERENCES "Catalog" (id)
);
CREATE TABLE "Catalog_description" (
	"Catalog_id" TEXT, 
	description TEXT NOT NULL, 
	PRIMARY KEY ("Catalog_id", description), 
	FOREIGN KEY("Catalog_id") REFERENCES "Catalog" (id)
);
CREATE TABLE "ObjectOfInterest_name" (
	"ObjectOfInterest_id" TEXT, 
	name TEXT, 
	PRIMARY KEY ("ObjectOfInterest_id", name), 
	FOREIGN KEY("ObjectOfInterest_id") REFERENCES "ObjectOfInterest" (id)
);
CREATE TABLE "ObjectOfInterest_description" (
	"ObjectOfInterest_id" TEXT, 
	description TEXT, 
	PRIMARY KEY ("ObjectOfInterest_id", description), 
	FOREIGN KEY("ObjectOfInterest_id") REFERENCES "ObjectOfInterest" (id)
);
CREATE TABLE "Tool_name" (
	"Tool_id" TEXT, 
	name TEXT, 
	PRIMARY KEY ("Tool_id", name), 
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id)
);
CREATE TABLE "Tool_description" (
	"Tool_id" TEXT, 
	description TEXT, 
	PRIMARY KEY ("Tool_id", description), 
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id)
);
CREATE TABLE "Dataset_name" (
	"Dataset_id" TEXT, 
	name TEXT NOT NULL, 
	PRIMARY KEY ("Dataset_id", name), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "Dataset_description" (
	"Dataset_id" TEXT, 
	description TEXT NOT NULL, 
	PRIMARY KEY ("Dataset_id", description), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);