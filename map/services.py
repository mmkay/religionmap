from collections import Counter

import overpass

from map.util.iterate import seq


class OverpassService:
    def __init__(self):
        self.api = overpass.API()

    def get_temples_tiled(self, lat, lon, span):
        temples_data = []
        split_span_into = 3.0
        print(seq(lat - span, lat + span, span / split_span_into))
        for lat_step in seq(lat - span, lat + span, span / split_span_into):
            for lon_step in seq(lon - span, lon + span, span / split_span_into):
                temples_data.append(self.get_temples(lat_step, lon_step, span / split_span_into))
        return temples_data

    def get_temples(self, lat, lon, span):
        print("Search for lat: %f, lon: %f, span: %f" % (lat, lon, span))
        lat_top = lat - span
        lat_bottom = lat + span
        lon_top = lon - span
        lon_bottom = lon + span
        query = '(way[\"amenity\"=\"place_of_worship\"](%f,%f,%f,%f);>;node[\"amenity\"=\"place_of_worship\"](%f,%f,%f,%f););' % (
        lat_top, lon_top, lat_bottom, lon_bottom, lat_top, lon_top, lat_bottom, lon_bottom)
        print("query: %s" % query)
        geojson = self.api.Get(query)
        temples = filter(
            lambda element: u'amenity' in element and element[u'amenity'] == u'place_of_worship',
            map(
                lambda x: x.properties,
                filter(lambda x: bool(x.properties), geojson.features)
            )
        )
        by_religion = dict(Counter(map(
            lambda element: element[u'religion'],
            filter(lambda element: u'religion' in element, temples)
        )))
        by_denomination = dict(Counter(map(
            lambda element: element[u'denomination'],
            filter(lambda element: u'denomination' in element, temples)
        )))
        return {
            "lat": lat,
            "lon": lon,
            "span": span,
            "count": len(temples),
            "by_religion": by_religion,
            "by_denomination": by_denomination,
            "temples": temples
        }
