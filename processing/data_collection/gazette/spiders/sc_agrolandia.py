from gazette.spiders.base import FecamGazetteSpider


class ScAgrolandiaSpider(FecamGazetteSpider):
    name = "sc_agrolandia"
    FECAM_QUERY = 'entidade:"Prefeitura Municipal de Agrolândia"'
    TERRITORY_ID = "4200200"