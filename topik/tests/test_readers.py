import os
import unittest

from topik.readers import read_input

# sample data files are located in the same folder
module_path = os.path.dirname(__file__)


class TestReader(unittest.TestCase):

    def setUp(self):
        self.solution_1 = str("'Interstellar' was incredible. The visuals, the score, the acting, were all amazing."
                              " The plot is definitely one of the most original I've seen in a while.")
        self.solution_2 = str('In this paper, we describe a simple and rapid solution-phase chemical reduction method'
                              ' with no inert gas protection, for preparing stable copper nanoparticle colloid with'
                              ' average particle size of 3.4 nm and narrow size distribution. In our synthesis route,'
                              ' ascorbic acid, natural vitamin C (VC), serves as both a reducing agent and an'
                              ' antioxidant to reduce copper salt precursor and effectively prevent the general'
                              ' oxidation process occurring to the newborn nanoparticles. XRD and UV/vis confirm the'
                              ' formation of pure face-centered cubic (fcc) copper nanoparticles and the excellent'
                              ' antioxidant ability of ascorbic acid.')


    def test_read_document_json_stream(self):
        iterable_data = read_input(os.path.join(module_path, 'data/test-data-1.json'),
                                   content_field="text",
                                   output_type="dictionary")
        id, first_text = next(iter(iterable_data))
        self.assertEqual(first_text, self.solution_1)

    def test_read_document_json_stream_with_year_field(self):
        raise NotImplementedError("TODO: need data source that actually has date data!  test-data-1.json does not!")
        iterable_data = _iter_document_json_stream(
                os.path.join(module_path, 'data/test-data-1.json'))
        first_text = next(iterable_data)
        self.assertEqual(first_text, self.solution_1)

    def test_read_documents_folder(self):
        loaded_dictionaries = read_input(
            os.path.join(module_path, 'data/test-data-folder'),
            content_field="abstract",
            output_type="dictionary")
        id, first_text = next(iter(loaded_dictionaries))
        self.assertEqual(first_text, self.solution_1)

    def test_iter_documents_folder_gz(self):
        loaded_dictionaries = read_input(
            os.path.join(module_path, 'data/test-data-folder-gz'),
            content_field="abstract",
            output_type="dictionary")
        id, first_text = next(iter(loaded_dictionaries))
        self.assertEqual(first_text, self.solution_1)

    def test_iter_large_json(self):
        iterable_data = read_input(os.path.join(module_path, 'data/test-data-2.json'),
                                   content_field="abstract",
                                   output_type="dictionary")
        id, first_text = next(iter(iterable_data))
        self.assertEqual(first_text, self.solution_2)

if __name__ == '__main__':
    unittest.main()
