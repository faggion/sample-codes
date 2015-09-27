# coding: utf-8

a = [1,[10,11,[100,101,102]],3]

dump_hoge(a,"")

BEGIN {
  def dump_hoge(aaa, indent)
    aaa.each do |aa|
      if aa.class == Fixnum
        puts indent+aa.to_s
      else
        dump_hoge(aa, indent+"  ")
      end
    end
  end
}
