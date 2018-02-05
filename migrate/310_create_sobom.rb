Sequel.migration do
  change do
     create_table(:sobom) do
      column :so_id, :varchar, :size => 10
      column :sordnum, :varchar, :size => 7
      column :soforecast, :boolean
      column :linenum, :integer
      column :relnum, :integer
      column :clevel, :integer
      column :clevel_lin, :varchar, :size => 2
      column :bomnode, :integer
      column :inventnum, :varchar, :size => 30
      column :invent_typ, :varchar, :size => 5
      column :partnum, :varchar, :size => 30
      column :make_buy, :varchar, :size => 4
      column :iv_supp_co, :varchar, :size => 6
      column :iv_planner, :varchar, :size => 5
      column :exclfrommr, :boolean
      column :purchunit, :varchar, :size => 2
      column :calctype, :varchar, :size => 2
      column :alloc, :boolean
      column :iv_stock_u, :varchar, :size => 15
      column :iv_purch_u, :varchar, :size => 15
      column :partcnt, :float
      column :partdesc, :varchar, :size => 50
      column :shipdate, :date
      column :duedate, :date
      column :promdate, :date
      column :shipbydate, :date
      column :fabdate, :date
      column :relqty, :float
      column :qtybal, :float
      column :qtyneed, :float
      column :qtytoprod, :float
      column :reolevel, :float
      column :reoqty, :float
      column :qtyonhand, :float
      column :leadtime, :integer
      column :startdate, :date
      column :enddate, :date
      column :parentp, :varchar, :size => 30
      column :level, :integer
      column :iv_date_1, :date
      column :iv_date_2, :date
      column :iv_date_3, :date
      column :iv_date_4, :date
      column :iv_date_5, :date
      column :iv_date_6, :date
      column :iv_date_7, :date
      column :iv_date_8, :date
      column :iv_date_9, :date
      column :iv_date_10, :date
      column :iv_date_11, :date
      column :iv_date_12, :date
      column :iv_date_13, :date
      column :iv_date_14, :date
      column :iv_date_15, :date
      column :iv_date_16, :date
      column :iv_date_17, :date
      column :iv_date_18, :date
      column :iv_date_19, :date
      column :iv_date_20, :date
      column :iv_date_21, :date
      column :iv_date_22, :date
      column :iv_date_23, :date
      column :iv_date_24, :date
      column :iv_date_25, :date
      column :iv_date_26, :date
      column :iv_date_27, :date
      column :iv_date_28, :date
      column :iv_date_29, :date
      column :iv_date_30, :date
      column :iv_date_31, :date
      column :iv_date_32, :date
      column :iv_date_33, :date
      column :iv_date_34, :date
      column :iv_date_35, :date
      column :iv_date_36, :date
      column :iv_qty_1, :float
      column :iv_qty_2, :float
      column :iv_qty_3, :float
      column :iv_qty_4, :float
      column :iv_qty_5, :float
      column :iv_qty_6, :float
      column :iv_qty_7, :float
      column :iv_qty_8, :float
      column :iv_qty_9, :float
      column :iv_qty_10, :float
      column :iv_qty_11, :float
      column :iv_qty_12, :float
      column :iv_qty_13, :float
      column :iv_qty_14, :float
      column :iv_qty_15, :float
      column :iv_qty_16, :float
      column :iv_qty_17, :float
      column :iv_qty_18, :float
      column :iv_qty_19, :float
      column :iv_qty_20, :float
      column :iv_qty_21, :float
      column :iv_qty_22, :float
      column :iv_qty_23, :float
      column :iv_qty_24, :float
      column :iv_qty_25, :float
      column :iv_qty_26, :float
      column :iv_qty_27, :float
      column :iv_qty_28, :float
      column :iv_qty_29, :float
      column :iv_qty_30, :float
      column :iv_qty_31, :float
      column :iv_qty_32, :float
      column :iv_qty_33, :float
      column :iv_qty_34, :float
      column :iv_qty_35, :float
      column :iv_qty_36, :float
      column :iv_onhand_, :float
      column :iv_onhand2, :float
      column :iv_onhand3, :float
      column :iv_onhand4, :float
      column :iv_onhand5, :float
      column :iv_onhand6, :float
      column :iv_onhand7, :float
      column :iv_onhand8, :float
      column :iv_onhand9, :float
      column :iv_onhan10, :float
      column :iv_onhan11, :float
      column :iv_onhan12, :float
      column :iv_onhan13, :float
      column :iv_onhan14, :float
      column :iv_onhan15, :float
      column :iv_onhan16, :float
      column :iv_onhan17, :float
      column :iv_onhan18, :float
      column :iv_onhan19, :float
      column :iv_onhan20, :float
      column :iv_onhan21, :float
      column :iv_onhan22, :float
      column :iv_onhan23, :float
      column :iv_onhan24, :float
      column :iv_onhan25, :float
      column :iv_onhan26, :float
      column :iv_onhan27, :float
      column :iv_onhan28, :float
      column :iv_onhan29, :float
      column :iv_onhan30, :float
      column :iv_onhan31, :float
      column :iv_onhan32, :float
      column :iv_onhan33, :float
      column :iv_onhan34, :float
      column :iv_onhan35, :float
      column :iv_onhan36, :float
      column :iv_balreq_, :float
      column :iv_balreq2, :float
      column :iv_balreq3, :float
      column :iv_balreq4, :float
      column :iv_balreq5, :float
      column :iv_balreq6, :float
      column :iv_balreq7, :float
      column :iv_balreq8, :float
      column :iv_balreq9, :float
      column :iv_balre10, :float
      column :iv_balre11, :float
      column :iv_balre12, :float
      column :iv_balre13, :float
      column :iv_balre14, :float
      column :iv_balre15, :float
      column :iv_balre16, :float
      column :iv_balre17, :float
      column :iv_balre18, :float
      column :iv_balre19, :float
      column :iv_balre20, :float
      column :iv_balre21, :float
      column :iv_balre22, :float
      column :iv_balre23, :float
      column :iv_balre24, :float
      column :iv_balre25, :float
      column :iv_balre26, :float
      column :iv_balre27, :float
      column :iv_balre28, :float
      column :iv_balre29, :float
      column :iv_balre30, :float
      column :iv_balre31, :float
      column :iv_balre32, :float
      column :iv_balre33, :float
      column :iv_balre34, :float
      column :iv_balre35, :float
      column :iv_balre36, :float
      column :iv_onorder, :float
      column :iv_onorde2, :float
      column :iv_onorde3, :float
      column :iv_onorde4, :float
      column :iv_onorde5, :float
      column :iv_onorde6, :float
      column :iv_onorde7, :float
      column :iv_onorde8, :float
      column :iv_onorde9, :float
      column :iv_onord10, :float
      column :iv_onord11, :float
      column :iv_onord12, :float
      column :iv_onord13, :float
      column :iv_onord14, :float
      column :iv_onord15, :float
      column :iv_onord16, :float
      column :iv_onord17, :float
      column :iv_onord18, :float
      column :iv_onord19, :float
      column :iv_onord20, :float
      column :iv_onord21, :float
      column :iv_onord22, :float
      column :iv_onord23, :float
      column :iv_onord24, :float
      column :iv_onord25, :float
      column :iv_onord26, :float
      column :iv_onord27, :float
      column :iv_onord28, :float
      column :iv_onord29, :float
      column :iv_onord30, :float
      column :iv_onord31, :float
      column :iv_onord32, :float
      column :iv_onord33, :float
      column :iv_onord34, :float
      column :iv_onord35, :float
      column :iv_onord36, :float
      column :so_po_num, :varchar, :size => 25
      column :ss_confirm, :boolean
    end
  end
end
