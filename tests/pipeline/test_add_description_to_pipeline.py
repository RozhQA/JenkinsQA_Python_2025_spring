from pages.pipeline_page import PipelinePage
from tests.pipeline.pipeline_data import description_text, pipeline_project_name


def test_add_description_to_pipeline(pipeline_config_page):
    pipeline_config_page.add_description(description_text)
    pipeline_config_page.click_save_button()

    pipeline_page = PipelinePage(pipeline_config_page.driver, pipeline_project_name)
    assert pipeline_page.desc_element_is_displayed(), "Description is not visible"

    desc_element_text = pipeline_page.get_description_text()
    assert desc_element_text == description_text, \
        f"Expected description '{description_text}', but got '{desc_element_text}'"