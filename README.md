# PythonSeleniumOdev
Bir fonksiyon başka bir fonksiyon döndüren @wrapper syntax ı ile çalışan yapı Decorator yapısıdır.Decorator lere en yaygın örneği classmethod() ve staticmethod()tir.
def f(arg):
    ...
f = staticmethod(f)

@staticmethod
def f(arg):
ikiside birbirine benzer.

Parametreli decorator zincirleme decorator olarak kullanılabilir.Arka arkaya decorator kullanımı zincirleme decorator olarak adlandırılır.
@benchmark=alttan gelen wrapper fonksiyonu ölçümü yapar.
@has_permission
@sleep()=bekleme süresi decorator
@pytest.mark.sanity
Sabitler
pytest.__version__
pytest.version_tuple
Fonksiyonlar
pytest.approx
pytest.fail
pytest.skip
pytest.importorskip
pytest.xfail
pytest.exit
pytest.main
pytest.param
pytest.raises
pytest.deprecated_call
pytest.register_assert_rewrite
pytest.warns
pytest.freeze_includes
İşaretleyici
pytest.mark.filterwarnings
pytest.mark.parametrize
pytest.mark.skip
pytest.mark.skipif
pytest.mark.usefixtures
pytest.mark.xfail
