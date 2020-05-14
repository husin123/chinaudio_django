from ocr.views import OcrView
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url

ocr_view = OcrView()

# admin.autodiscover()
urlpatterns = [
    path('index/', ocr_view.index),
    path('ocrPDF_assist_request/',ocr_view.ocrPDF_assist_request),
    path('ocrPDF_assist_request/sub_and_execute/',ocr_view.sub_and_execute_assist_ocr),
    path('ocrPDF_assist_in_deny/',ocr_view.ocrPDF_assist_request_deny),
    path('ocrPDF_assist_in_accept/',ocr_view.ocrPDF_assist_request_accept),
    path('delete_ocr_labeling/', ocr_view.delete_ocr_labeling),
    path('ocrPDF_assist_out_delete/',ocr_view.ocrPDF_assist_request_delete),
    path('addpdfs/', ocr_view.addpdfs),
    path('labeling/', ocr_view.labeling),
    path('labeling/get_image/', ocr_view.ocr_get_image),
    path('labeling/get_polygon_image/', ocr_view.get_polygon_image),
    path('labeling/get_elem_image/', ocr_view.get_elem_image),
    path('labeling/direction_select/', ocr_view.direction_select),
    path('labeling/set_filter_size/', ocr_view.set_filter_size),
    path('labeling/set_entropy_thr/', ocr_view.set_entropy_thr),
    path('labeling/save_anchor/', ocr_view.save_anchor),
    path('labeling/get_polygon_statistic/', ocr_view.get_polygon_statistic),
    path('labeling/move_page/', ocr_view.ocr_move_page),
    path('labeling/direction_pdf/', ocr_view.direction_pdf),
    path('labeling/rotate_degree_evaluate/', ocr_view.rotate_degree_evaluate),
    path('labeling/rotate_degree_reset/', ocr_view.rotate_degree_reset),
    path('labeling/add_labeling_polygon/', ocr_view.add_labeling_polygon),
    path('labeling/delete_all_polygon/', ocr_view.delete_all_polygon),
    path('labeling/entropy_thr_reset/', ocr_view.entropy_thr_reset),
    path('labeling/alter_polygon_by_id/', ocr_view.alter_polygon_by_id),
    path('labeling/delete_polygon_by_id/', ocr_view.delete_polygon_by_id),
    path('labeling/delete_region/', ocr_view.delete_region),
    path('labeling/merge_labeling/', ocr_view.merge_labeling),
    path('labeling/rough_labeling/', ocr_view.rough_labeling),
    path('content_labeling/', ocr_view.content_labeling),
    path('content_labeling/add_elem/', ocr_view.add_elem),
    path('content_labeling/achieve_elem_id/', ocr_view.achieve_elem_id),
    path('content_labeling/get_elem_page/', ocr_view.get_elem_page),
    path('content_labeling/delete_elem_by_id/', ocr_view.delete_elem_by_id),
    path('content_labeling/get_character_image/', ocr_view.get_character_image),
    path('content_labeling/add_character/', ocr_view.add_character),
    path('content_labeling/delete_character/', ocr_view.delete_character),
    path('content_labeling/achieve_characters_from_elem/', ocr_view.achieve_characters_from_elem),
    path('content_labeling/get_elem_selected/', ocr_view.get_elem_selected),
    path('content_labeling/character_assist_check/', ocr_view.character_assist_check),
    path('content_labeling/elem_selected_add/', ocr_view.elem_selected_add),
    path('content_labeling/elem_selected_delete/', ocr_view.elem_selected_delete),
    path('content_labeling/alter_polygon_by_id/', ocr_view.alter_polygon_by_id),
]
