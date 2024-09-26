# Auto generated from dcat_nfdi_ap.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-09-26T10:03:25
# Schema: dcat-NFDI-ap
#
# id: https://w3id.org/StroemPhi/dcat-NFDI-ap
# description: This is an extention of the DCAT Application Profile in LinkML. It is intended to be used by NFDI consortia as a core that can further be extended in profiles to provide domain specific metadata for a dataset.
# license: CC-BY 4.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
T4FS = CurieNamespace('T4FS', 'http://purl.obolibrary.org/obo/T4FS_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCAT = CurieNamespace('dcat', 'https://www.w3.org/ns/dcat#')
DCAT_NFDI_AP = CurieNamespace('dcat_nfdi_ap', 'https://w3id.org/StroemPhi/dcat-NFDI-ap/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = DCAT_NFDI_AP


# Types

# Class references
class NamedThingId(extended_str):
    pass


class DatasetId(NamedThingId):
    pass


class CatalogId(DatasetId):
    pass


class ObjectOfInterestId(NamedThingId):
    pass


class ToolId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = DCAT_NFDI_AP.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(NamedThing):
    """
    A collection of data, published or curated by a single agent, and available for access or download in one or more
    representations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = DCAT_NFDI_AP.Dataset

    id: Union[str, DatasetId] = None
    name: Union[str, List[str]] = None
    description: Union[str, List[str]] = None
    was_generated_by: Optional[Union[dict, "Activity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self.was_generated_by is not None and not isinstance(self.was_generated_by, Activity):
            self.was_generated_by = Activity(**as_dict(self.was_generated_by))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalog(Dataset):
    """
    A curated collection of metadata about data resources.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Catalog"
    class_model_uri: ClassVar[URIRef] = DCAT_NFDI_AP.Catalog

    id: Union[str, CatalogId] = None
    name: Union[str, List[str]] = None
    description: Union[str, List[str]] = None
    has_dataset: Optional[Union[Dict[Union[str, DatasetId], Union[dict, Dataset]], List[Union[dict, Dataset]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalogId):
            self.id = CatalogId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        self._normalize_inlined_as_list(slot_name="has_dataset", slot_type=Dataset, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Activity(YAMLRoot):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT_NFDI_AP["Activity"]
    class_class_curie: ClassVar[str] = "dcat_nfdi_ap:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = DCAT_NFDI_AP.Activity

    type: Optional[Union[str, "ActivityType"]] = None
    has_part: Optional[Union[dict, "Activity"]] = None
    had_object: Optional[Union[Dict[Union[str, ObjectOfInterestId], Union[dict, "ObjectOfInterest"]], List[Union[dict, "ObjectOfInterest"]]]] = empty_dict()
    used_tool: Optional[Union[Dict[Union[str, ToolId], Union[dict, "Tool"]], List[Union[dict, "Tool"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, ActivityType):
            self.type = ActivityType(self.type)

        if self.has_part is not None and not isinstance(self.has_part, Activity):
            self.has_part = Activity(**as_dict(self.has_part))

        self._normalize_inlined_as_list(slot_name="had_object", slot_type=ObjectOfInterest, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_tool", slot_type=Tool, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObjectOfInterest(NamedThing):
    """
    Something that is being observed, studied, modified, influenced or consumed within an activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT_NFDI_AP["ObjectOfInterest"]
    class_class_curie: ClassVar[str] = "dcat_nfdi_ap:ObjectOfInterest"
    class_name: ClassVar[str] = "ObjectOfInterest"
    class_model_uri: ClassVar[URIRef] = DCAT_NFDI_AP.ObjectOfInterest

    id: Union[str, ObjectOfInterestId] = None
    type: Optional[Union[str, "ObjectType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObjectOfInterestId):
            self.id = ObjectOfInterestId(self.id)

        if self.type is not None and not isinstance(self.type, ObjectType):
            self.type = ObjectType(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tool(NamedThing):
    """
    Something with a certain function used within an activity to achieve the overall goal of the activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT_NFDI_AP["Tool"]
    class_class_curie: ClassVar[str] = "dcat_nfdi_ap:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = DCAT_NFDI_AP.Tool

    id: Union[str, ToolId] = None
    type: Optional[Union[str, "ToolType"]] = None
    has_part: Optional[Union[str, ToolId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ToolId):
            self.id = ToolId(self.id)

        if self.type is not None and not isinstance(self.type, ToolType):
            self.type = ToolType(self.type)

        if self.has_part is not None and not isinstance(self.has_part, ToolId):
            self.has_part = ToolId(self.has_part)

        super().__post_init__(**kwargs)


# Enumerations
class ActivityType(EnumDefinitionImpl):
    """
    An enum to provided allowed values for the type of an Activity.
    """
    data_curation = PermissibleValue(
        text="data_curation",
        description="""A managed process, throughout the data lifecycle, by which data & data collections are cleansed, documented, standardized, formatted and inter-related. This includes versioning data, or forming a new collection from several data sources, annotating with metadata, adding codes to raw data (e.g., classifying a galaxy image with a galaxy type such as spiral).""",
        meaning=T4FS["0000132"])
    spectroscopy = PermissibleValue(
        text="spectroscopy",
        description="""The study of the interaction of a sample with radiation or particles for measurement or detection.""",
        meaning=CHMO["0000228"])

    _defn = EnumDefinition(
        name="ActivityType",
        description="An enum to provided allowed values for the type of an Activity.",
    )

class ObjectType(EnumDefinitionImpl):
    """
    An enum to provide the allowed values for the type of an Object.
    """
    cola = PermissibleValue(
        text="cola",
        description="""SIREN DB annotation: * liquid, low viscosity, with no visible particles food (liquid, low viscosity, with no visible particles) * fully heat-treated fully heat-treated * artificially carbonated artificial carbonation process * acidified acidification process * ingredient: sugar or sugar syrup added obsolete: sugar or sugar syrup added * ingredient: color added food color addition process * ingredient: flavoring, spice or herb added flavoring, spice or herb""",
        meaning=FOODON["03301776"])

    _defn = EnumDefinition(
        name="ObjectType",
        description="An enum to provide the allowed values for the type of an Object.",
    )

class ToolType(EnumDefinitionImpl):
    """
    An enum to provide the allowed values for the type of a Tool.
    """
    spectrometer = PermissibleValue(
        text="spectrometer",
        description="A piece of apparatus used to measure a spectrum.",
        meaning=CHMO["0001234"])

    _defn = EnumDefinition(
        name="ToolType",
        description="An enum to provide the allowed values for the type of a Tool.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=DCAT_NFDI_AP.id, name="id", curie=DCAT_NFDI_AP.curie('id'),
                   model_uri=DCAT_NFDI_AP.id, domain=None, range=URIRef)

slots.name = Slot(uri=DCT.title, name="name", curie=DCT.curie('title'),
                   model_uri=DCAT_NFDI_AP.name, domain=None, range=Optional[Union[str, List[str]]])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=DCAT_NFDI_AP.description, domain=None, range=Optional[Union[str, List[str]]])

slots.type = Slot(uri=DCT.type, name="type", curie=DCT.curie('type'),
                   model_uri=DCAT_NFDI_AP.type, domain=None, range=Optional[str])

slots.has_part = Slot(uri=DCAT_NFDI_AP.has_part, name="has_part", curie=DCAT_NFDI_AP.curie('has_part'),
                   model_uri=DCAT_NFDI_AP.has_part, domain=None, range=Optional[str])

slots.dataset__was_generated_by = Slot(uri=DCAT_NFDI_AP.was_generated_by, name="dataset__was_generated_by", curie=DCAT_NFDI_AP.curie('was_generated_by'),
                   model_uri=DCAT_NFDI_AP.dataset__was_generated_by, domain=None, range=Optional[Union[dict, Activity]])

slots.catalog__has_dataset = Slot(uri=DCAT.dataset, name="catalog__has_dataset", curie=DCAT.curie('dataset'),
                   model_uri=DCAT_NFDI_AP.catalog__has_dataset, domain=None, range=Optional[Union[Dict[Union[str, DatasetId], Union[dict, Dataset]], List[Union[dict, Dataset]]]])

slots.activity__had_object = Slot(uri=DCAT_NFDI_AP.had_object, name="activity__had_object", curie=DCAT_NFDI_AP.curie('had_object'),
                   model_uri=DCAT_NFDI_AP.activity__had_object, domain=None, range=Optional[Union[Dict[Union[str, ObjectOfInterestId], Union[dict, ObjectOfInterest]], List[Union[dict, ObjectOfInterest]]]])

slots.activity__used_tool = Slot(uri=DCAT_NFDI_AP.used_tool, name="activity__used_tool", curie=DCAT_NFDI_AP.curie('used_tool'),
                   model_uri=DCAT_NFDI_AP.activity__used_tool, domain=None, range=Optional[Union[Dict[Union[str, ToolId], Union[dict, Tool]], List[Union[dict, Tool]]]])

slots.Dataset_id = Slot(uri=DCAT_NFDI_AP.id, name="Dataset_id", curie=DCAT_NFDI_AP.curie('id'),
                   model_uri=DCAT_NFDI_AP.Dataset_id, domain=Dataset, range=Union[str, DatasetId])

slots.Dataset_name = Slot(uri=DCT.title, name="Dataset_name", curie=DCT.curie('title'),
                   model_uri=DCAT_NFDI_AP.Dataset_name, domain=Dataset, range=Union[str, List[str]])

slots.Dataset_description = Slot(uri=DCT.description, name="Dataset_description", curie=DCT.curie('description'),
                   model_uri=DCAT_NFDI_AP.Dataset_description, domain=Dataset, range=Union[str, List[str]])

slots.Catalog_id = Slot(uri=DCAT_NFDI_AP.id, name="Catalog_id", curie=DCAT_NFDI_AP.curie('id'),
                   model_uri=DCAT_NFDI_AP.Catalog_id, domain=Catalog, range=Union[str, CatalogId])

slots.Catalog_name = Slot(uri=DCT.title, name="Catalog_name", curie=DCT.curie('title'),
                   model_uri=DCAT_NFDI_AP.Catalog_name, domain=Catalog, range=Union[str, List[str]])

slots.Catalog_description = Slot(uri=DCT.description, name="Catalog_description", curie=DCT.curie('description'),
                   model_uri=DCAT_NFDI_AP.Catalog_description, domain=Catalog, range=Union[str, List[str]])

slots.Activity_type = Slot(uri=DCT.type, name="Activity_type", curie=DCT.curie('type'),
                   model_uri=DCAT_NFDI_AP.Activity_type, domain=Activity, range=Optional[Union[str, "ActivityType"]])

slots.Activity_has_part = Slot(uri=DCAT_NFDI_AP.has_part, name="Activity_has_part", curie=DCAT_NFDI_AP.curie('has_part'),
                   model_uri=DCAT_NFDI_AP.Activity_has_part, domain=Activity, range=Optional[Union[dict, "Activity"]])

slots.ObjectOfInterest_type = Slot(uri=DCT.type, name="ObjectOfInterest_type", curie=DCT.curie('type'),
                   model_uri=DCAT_NFDI_AP.ObjectOfInterest_type, domain=ObjectOfInterest, range=Optional[Union[str, "ObjectType"]])

slots.Tool_type = Slot(uri=DCT.type, name="Tool_type", curie=DCT.curie('type'),
                   model_uri=DCAT_NFDI_AP.Tool_type, domain=Tool, range=Optional[Union[str, "ToolType"]])

slots.Tool_has_part = Slot(uri=DCAT_NFDI_AP.has_part, name="Tool_has_part", curie=DCAT_NFDI_AP.curie('has_part'),
                   model_uri=DCAT_NFDI_AP.Tool_has_part, domain=Tool, range=Optional[Union[str, ToolId]])