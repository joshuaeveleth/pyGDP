from pyGDP_WFS_Utilities import shapefile_value_handle

def getGMLIDs(shapefile, attribute, value):
    """
    This function returns the gmlID associated with a particular attribute value.
    """
    tuples = getTuples(shapefile, attribute)
    return _getFilterID(tuples, value)

def getTuples(shapefile, attribute):
    """
    Will return the dictionary tuples only.
    """
    return shapefile_value_handle.getValues(shapefile, attribute, getTuples='only', limitFeatures=None)

def _getFilterID(tuples, value):
    """
    Given a the tuples generated by getTuples and a value, will return a list of gmlIDs
    associated with the value specified.
    """
    value = str(value)
    filterID = []
    for item in tuples:
        if item[0] == value:
            filterID.append(item[1])
    if filterID==[]:
        raise Exception('Feature attribute value %s was not found in the feature collection.' % value)
    return filterID
