import struct

class ctaJPA:
    def __init__(self, file_path):
        self.file_path = file_path
        self.jfif_header = b'\xFF\xD8\xFF\xE0'
        self.binary_data = b''

    def read_jpa_file(self):
        with open(self.file_path, 'rb') as file:
            file_content = file.read()

            # Find the JFIF header
            jfif_start = file_content.find(self.jfif_header)
            if jfif_start == -1:
                raise ValueError("Invalid JPA file. JFIF header not found.")

            # Extract the binary data
            binary_start = jfif_start + len(self.jfif_header)
            self.binary_data = file_content[binary_start:]

    def write_jpg_file(self, output_path):
        with open(output_path, 'wb') as file:
            file.write(self.jfif_header)
            file.write(self.binary_data)

    def get_binary_data(self):
        return self.binary_data

    def set_binary_data(self, data):
        self.binary_data = data


# Example usage for read function

jpa_instance = ctaJPA('test.jpa')
jpa_instance.read_jpa_file()
binary_data = jpa_instance.get_binary_data()

# Save as JPG
output_path = 'output.jpg'  # Specify the output file path
jpa_instance.write_jpg_file(output_path)
