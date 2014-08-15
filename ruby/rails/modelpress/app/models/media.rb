class Media < ActiveRecord::Base
  validates :name, presence: true
end
