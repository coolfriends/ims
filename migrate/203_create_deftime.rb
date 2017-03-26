Sequel.migration do
  change do
     create_table(:deftime) do
      column :s1_ci, :varchar, :size => 10
      column :s1_co, :varchar, :size => 10
      column :s1_lo, :varchar, :size => 10
      column :s1_li, :varchar, :size => 10
      column :s2_ci, :varchar, :size => 10
      column :s2_co, :varchar, :size => 10
      column :s2_lo, :varchar, :size => 10
      column :s2_li, :varchar, :size => 10
      column :s3_ci, :varchar, :size => 10
      column :s3_co, :varchar, :size => 10
      column :s3_lo, :varchar, :size => 10
      column :s3_li, :varchar, :size => 10
      column :r_limit, :integer
      column :jc_use, :varchar, :size => 1
      column :tc_use, :varchar, :size => 1
      column :minlunch, :integer
      column :animatetc, :boolean
      column :s_flag, :boolean
      column :td_flag, :boolean
      column :od_flag, :boolean
      column :bp_flag, :boolean
      column :bu_flag, :boolean
      column :lp_flag, :boolean
      column :lu_flag, :boolean
      column :qty_only_f, :boolean
      column :qty_review, :boolean
      column :qty_rework, :boolean
      column :qty_scrap, :boolean
      column :paperless, :boolean
      column :changetime, :boolean
      column :swipe_only, :boolean
      column :use_tscree, :boolean
      column :use_tcards, :boolean
      column :use_jcards, :boolean
      column :allow_shif, :boolean
      column :select_co_, :boolean
      column :ripple_rel, :boolean
      column :secure_am, :boolean
      column :supervisor, :boolean
      column :disable_jc, :boolean
      column :secure_exi, :boolean
      column :round15, :boolean
      column :digits_onl, :boolean
      column :sort_by_la, :boolean
      column :no_emp_lis, :boolean
      column :dont_close, :boolean
      column :tcard_thre, :integer
      column :remove_key, :boolean
      column :simple_jc, :boolean
      column :consolidat, :boolean
      column :at_hours_a, :float
      column :ot_hours_a, :float
      column :le_leaves_, :integer
      column :manual_jc, :boolean
      column :timeserver, :varchar, :size => 30
      column :bypassmatr, :boolean
      column :close_on_l, :boolean
      column :mon_refres, :integer
      column :wp_export_, :varchar, :size => 12
      column :wp_export2, :varchar, :size => 40
      column :remain_in_, :boolean
      column :le_use_no_, :boolean
      column :use_timecl, :boolean
      column :enforce_30, :boolean
      column :deptoverri, :boolean
      column :use_1_x2_bi, :boolean
      column :jobonly, :boolean
      column :eo_hours_a, :boolean
      column :hide_jc, :boolean
      column :sublot, :boolean
      column :round15_lu, :boolean
      column :hide_add_o, :boolean
      column :nojcwithou, :boolean
      column :nojcwithjc, :boolean
      column :notcwithjc, :boolean
      column :op_comp_fl, :boolean
      column :endofshift, :boolean
      column :quickjob, :boolean
      column :defaultqty, :boolean
      column :autojcout, :integer
      column :autooverti, :boolean
      column :showdie, :boolean
      column :diereport, :boolean
      column :showheat, :boolean
      column :at_include, :boolean
      column :roundjobca, :boolean
      column :round78, :boolean
      column :clockoutpr, :boolean
      column :use_small_, :boolean
      column :autosave, :boolean
      column :nonpmultij, :boolean
      column :showlot_nu, :boolean
      column :roundtc15, :boolean
      column :always15, :boolean
      column :cycleonly, :boolean
      column :barcodekey, :boolean
      column :usecounter, :boolean
      column :showpace, :boolean
      column :showpaceba, :text
      column :showpacego, :text
      column :showtag, :boolean
      column :usetagasbi, :boolean
      column :teamlogin, :boolean
      column :hidelaborc, :boolean
      column :usetcdate, :boolean
      column :showtrilab, :boolean
      column :usefactors, :boolean
      column :alwayslunc, :boolean
      column :empasteris, :boolean
      column :jcfirst, :boolean
      column :nodecimals, :boolean
      column :stoponhold, :boolean
      column :autofilllu, :boolean
      column :simplejc, :boolean
      column :eci_thresh, :integer
      column :eci_messag, :text
      column :defectcode, :boolean
      column :actionrequ, :boolean
      column :pausestart, :boolean
      column :printbinti, :boolean
      column :calc_perce, :boolean
      column :defaultmat, :boolean
    end
  end
end
