def load_library(NAME_LIB, FILE_PATH, local=False):
    from importlib.machinery import SourceFileLoader

    if local==False:
        FILE_PATH = '/content/dissertacao/' + FILE_PATH

    else:
        FILE_PATH = '../../' + FILE_PATH


    somemodule = SourceFileLoader(NAME_LIB, FILE_PATH).load_module()
    





def get_libs(local=False):
    #folder notebooks
    #load_library('paths', 'notebooks/Baseline/paths.py')

    
    #folder src.data
    load_library('make_dataset', 'src/data/make_dataset.py', local=local)


    #folder src.models
    load_library('train_model', 'src/models/train_model.py', local=local)
    load_library('evaluation', 'src/models/evaluation.py', local=local)
    load_library('rank_cv', 'src/models/rank_cv.py', local=local)
    load_library('meta_model', 'src/models/meta_model.py', local=local)

    #folder src.validation (MANTER A ORDEM)
    load_library('group_ts_split', 'src/validation/group_ts_split.py', local=local)
    load_library('metrics_description', 'src/validation/metrics_description.py', local=local)
    load_library('metrics', 'src/validation/metrics.py', local=local)

    #folder src.visualization
    load_library('visualize', 'src/visualization/visualize.py', local=local)