from rest_framework import serializers
from nights_noroeste.models import NightsNoroeste

class NightsNoroesteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NightsNoroeste
        fields = ['farm_origen', 'is_active', 'tpp_s1','xaratanga_1','ctg_xaratanga','porcina_3','porcina_4_5','tpp_3_0_1','tpp_3_0_2','tpp_3_0_3','tpp_3_0_4','tpp_3_0_5','xaratanga_s2','xaratanga_cmg','seccion_10','porcina_9','laguna_1','laguna_2','querobabi','porcina_6','porcina_1','seccion_2','porcina_2','porcina_7','luis_emilio','maria_emma','ludi','porcina_10','elsa','la_palma','guaymita','xaratanga_3','c_mezquite','c_obregon','c_huatabampo','oficina_generales','almacen_general','planta_alimentos','plata_tif_227','venta_resaga']
        #depth = 1 para que me traiga todas las relaciones en json
