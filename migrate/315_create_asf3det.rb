Sequel.migration do
  change do
     create_table(:asf3det) do
      column :f3_det_id, :varchar, :size => 10
      column :char_num, :varchar, :size => 10
      column :reference_, :varchar, :size => 30
      column :char_desig, :varchar, :size => 30
      column :results, :varchar, :size => 50
      column :design_too, :varchar, :size => 30
      column :nonconf_nu, :varchar, :size => 30
      column :meas_gauge, :varchar, :size => 50
      column :comments, :text
      column :as_id, :varchar, :size => 10
      column :asf3_id, :varchar, :size => 10
      column :requiremen, :varchar, :size => 50
    end
  end
end
