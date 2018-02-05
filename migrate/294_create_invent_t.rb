Sequel.migration do
  change do
     create_table(:invent_t) do
      column :it_invent_, :varchar, :size => 5
      column :it_invent2, :varchar, :size => 20
      column :it_rgb, :integer
      column :it_dontred, :boolean
    end
  end
end
