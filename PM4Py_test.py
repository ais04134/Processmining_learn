import pm4py
from pm4py.visualization.bpmn import visualizer as bpmn_visualizer


bpmn_graph = pm4py.read_bpmn(r"C:\Users\is041\geon_hyeon\PM4py\pm4py-core-release\pm4py-core-release\tests\input_data\running-example.bpmn")
gviz = bpmn_visualizer.apply(bpmn_graph)
bpmn_visualizer.view(gviz)