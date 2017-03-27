# frozen_string_literal: true

Sequel.migration do
  change do
    create_table(:py_fedtx) do
      column :ft_date, :date
      column :ft_taxes, :float
    end
  end
end
