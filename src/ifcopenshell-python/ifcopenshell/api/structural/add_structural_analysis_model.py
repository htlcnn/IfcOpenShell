import ifcopenshell
from ifcopenshell.api.owner.api import create_owner_history


class Usecase:
    def __init__(self, file, settings={}):
        self.file = file
        self.settings = {}
        for key, value in settings.items():
            self.settings[key] = value

    def execute(self):
        return self.file.create_entity("IfcStructuralAnalysisModel", **{
            "GlobalId": ifcopenshell.guid.new(),
            "OwnerHistory": create_owner_history(),
            "Name": "Unnamed",
            "PredefinedType": "LOADING_3D"
        })