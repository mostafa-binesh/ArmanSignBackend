from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    """
    If pagination was available for the data, return the data as it is.
    If pagination was not available, wrap the data in a 'data' key.
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Check if data contains paginated structure
        if isinstance(data, dict) and 'results' in data:
            # Pagination keys detected; keep the data structure as is
            response_data = data
        else:
            # Non-paginated data; wrap in 'data'
            response_data = {'data': data}

        # Call super to render the data into the content type specified by the renderer
        return super(CustomJSONRenderer, self).render(response_data, accepted_media_type, renderer_context)