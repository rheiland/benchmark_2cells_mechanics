# benchmark_2cells_mechanics

In the PhysiCell-x-x-x directory, run `make` then run `project` (which will use the default `config/PhysiCell_settings.xml` model). Output intervals are 0.1 (same as mechanics dt). Note that the "persistence time" for motility is 0.

The critical function is `custom_function` in custom_modules/custom.cpp. Currently it just uses a hack for sufficient overlap of the 2 cells instead of `when the 2 cells "overlap by 10% of their volume", remove the force on each`.
