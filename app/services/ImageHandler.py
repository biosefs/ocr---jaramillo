class ImageHandler:    
    def __init__(self):
        self._current_image_path = None

    @property
    def image_path(self):
        """Get the current image path."""
        return self._current_image_path

    def load_image(self, path):
        """Set the current image path."""
        self._current_image_path = path

    def clear(self):  
        """Reset the image path."""
        self._current_image_path = None