""" Absorption calculator related tests
"""
from pytest import approx

from solcore import material, si
from solcore.structure import Structure, Layer
from solcore.absorption_calculator import create_adachi_alpha
from solcore.absorption_calculator import (
    calculate_rat,
    calculate_ellipsometry,
    calculate_absorption_profile,
)
from solcore.absorption_calculator.dielectric_constant_models import (
    DielectricConstantModel,
    Drude,
)
import numpy as np


def test_adachi_absorption():
    material_name = "InGaAs"
    solcore_material = material(material_name)(T=300, In=0.1)

    E, nn, kk, adachi_alpha_data = create_adachi_alpha(solcore_material, T=300)

    E /= 1.6e-19

    idx = np.argmin(abs(E - 2))

    out = [E[idx], nn[idx], kk[idx]]

    data = [2.0003267755918639, 3.6288603412514253, 0.30754355994545018]

    assert all([d == approx(o) for d, o in zip(data, out)])


def test_TMM_rat():
    GaAs = material("GaAs")(T=300)

    my_structure = Structure([Layer(si(3000, "nm"), material=GaAs)])

    wavelength = np.linspace(450, 1100, 300)
    idx = np.argmin(abs(wavelength - 800))

    out = calculate_rat(
        my_structure, wavelength, coherent=True, no_back_reflexion=False
    )
    out = (out["R"][idx], out["A"][idx], out["T"][idx])

    data = (0.33328918841743332, 0.65996607786373396, 0.0067447337188326914)

    assert all([d == approx(o) for d, o in zip(data, out)])


def test_TMM_absorption_profile():
    GaAs = material("GaAs")(T=300)

    my_structure = Structure(
        [Layer(si(3000, "nm"), material=GaAs), Layer(si(300, "um"), material=GaAs)]
    )

    out = calculate_absorption_profile(
        my_structure, np.array([800]), z_limit=3000, steps_size=20
    )

    data = (
        0.00093920198054733134,
        0.00091329190431268755,
        0.00088809661793623094,
        0.00086359640227330484,
        0.00083977208217782804,
        0.00081660501149482764,
        0.0007940770584669893,
        0.00077217059154379222,
        0.00075086846558214263,
        0.00073015400842769127,
        0.00071001100786633451,
        0.00069042369893569059,
        0.00067137675158661923,
        0.00065285525868512457,
        0.00063484472434525627,
        0.00061733105258387328,
        0.00060030053628839001,
        0.00058373984648887986,
        0.00056763602192612503,
        0.00055197645890746013,
        0.00053674890144246557,
        0.0005219414316507909,
        0.00050754246043459913,
        0.00049354071840833585,
        0.00047992524707871981,
        0.00046668539026805409,
        0.0004538107857741483,
        0.00044129135726031623,
        0.00042911730636911071,
        0.00041727910505361793,
        0.00040576748812031177,
        0.00039457344597762961,
        0.00038368821758459675,
        0.00037310328359397839,
        0.00036281035968459497,
        0.00035280139007758007,
        0.00034306854123150837,
        0.00033360419571145685,
        0.00032440094622720458,
        0.00031545158983589954,
        0.00030674912230466134,
        0.00029828673262870248,
        0.00029005779770068137,
        0.00028205587712711315,
        0.00027427470818778237,
        0.00026670820093421067,
        0.00025935043342334711,
        0.00025219564708274435,
        0.00024523824220360293,
        0.00023847277355814448,
        0.00023189394613789383,
        0.00022549661100952902,
        0.0002192757612850577,
        0.00021322652820316562,
        0.00020734417731867015,
        0.00020162410479709653,
        0.00019606183381147725,
        0.00019065301103855347,
        0.0001853934032516379,
        0.00018027889400747007,
        0.00017530548042447405,
        0.00017046927004989423,
        0.00016576647781335848,
        0.00016119342306448588,
        0.00015674652669221659,
        0.00015242230832361372,
        0.00014821738359994165,
        0.00014412846152789071,
        0.00014015234190387394,
        0.00013628591280938143,
        0.00013252614817542982,
        0.0001288701054142039,
        0.00012531492311603331,
        0.00012185781880990432,
        0.00011849608678575335,
        0.00011522709597683633,
        0.00011204828790051968,
        0.00010895717465587773,
        0.00010595133697653208,
        0.00010302842233720751,
        0.00010018614311252307,
        9.7422274786577231e-05,
        9.4734654211925496e-05,
        9.2121177916588886e-05,
        8.9579800457766819e-05,
        8.7108532820967001e-05,
        8.470544086329888e-05,
        8.2368643799712795e-05,
        8.009631273099949e-05,
        7.7886669212397987e-05,
        7.573798386169243e-05,
        7.3648575005706959e-05,
        7.1616807364140996e-05,
        6.9641090769713272e-05,
        6.7719878923614451e-05,
        6.5851668185292527e-05,
        6.4034996395625842e-05,
        6.2268441732560816e-05,
        6.0550621598319883e-05,
        5.8880191537308663e-05,
        5.7255844183874585e-05,
        5.5676308239094561e-05,
        5.41403474757902e-05,
        5.2646759770991723e-05,
        5.1194376165094236e-05,
        4.9782059946968693e-05,
        4.8408705764312587e-05,
        4.7073238758543685e-05,
        4.5774613723559514e-05,
        4.4511814287704784e-05,
        4.3283852118305772e-05,
        4.2089766148149713e-05,
        4.0928621823303459e-05,
        3.9799510371682887e-05,
        3.8701548091800482e-05,
        3.7633875661134488e-05,
        3.6595657463578247e-05,
        3.5586080935443529e-05,
        3.4604355929505788e-05,
        3.3649714096593824e-05,
        3.2721408284239568e-05,
        3.1818711951917646e-05,
        3.0940918602416916e-05,
        3.0087341228898868e-05,
        2.9257311777210295e-05,
        2.8450180623029266e-05,
        2.7665316063435288e-05,
        2.6902103822505617e-05,
        2.6159946570550893e-05,
        2.5438263456613905e-05,
        2.4736489653865175e-05,
        2.4054075917540213e-05,
        2.3390488155071715e-05,
        2.2745207008081107e-05,
        2.211772744590139e-05,
        2.1507558370314028e-05,
        2.0914222231189692e-05,
        2.0337254652732693e-05,
        1.9776204070036316e-05,
        1.9230631375664536e-05,
        1.8700109575983667e-05,
        1.8184223456974879e-05,
        1.7682569259266036e-05,
        1.7194754362128619e-05,
        1.6720396976192213e-05,
        1.6259125844636267e-05,
        1.5810579952625165e-05,
        1.5374408244759177e-05,
        1.4950269350320186e-05,
        1.4537831316097222e-05,
    )

    assert all([d == approx(o) for d, o in zip(data, out["absorption"][0])])


def test_TMM_ellipsometry():
    GaAs = material("GaAs")(T=300)

    my_structure = Structure(
        [Layer(si(3000, "nm"), material=GaAs), Layer(si(300, "um"), material=GaAs)]
    )

    wavelength = np.linspace(450, 1100, 300)
    idx = np.argmin(abs(wavelength - 800))

    angles = [60, 65, 70]
    out = calculate_ellipsometry(my_structure, wavelength, angle=angles)

    data = (
        22.2849089096,
        181.488417672,
        16.4604621886,
        182.277656469,
        9.10132195668,
        184.509752582,
    )

    for i in range(len(angles)):
        assert data[2 * i] == approx(out["psi"][idx, i])
        assert data[2 * i + 1] == approx(out["Delta"][idx, i])


def test_TMM_dielectric_model():
    drud = Drude(An=24.317000, Brn=0.125740)

    model = DielectricConstantModel(e_inf=3.4837, oscillators=[drud])

    wavelength = 2 * np.logspace(3, 4, 10)
    n = model.n_and_k(wavelength)

    data = (
        0.37377710 + 2.0726883j,
        0.53555835 + 3.03640188j,
        0.81383835 + 4.12781828j,
        1.25563998 + 5.39395751j,
        1.92396319 + 6.8504966j,
        2.88306008 + 8.48061105j,
        4.17692618 + 10.23820188j,
        5.81068443 + 12.06785126j,
        7.75184851 + 13.93546615j,
        9.95389660 + 15.84816722j,
    )

    assert all([d == approx(o) for d, o in zip(data, n)])


def test_sopra_absorption():
    from solcore.absorption_calculator import sopra_database

    # Import material constant data for Gallium Arsenide :: Do this by placing the
    # material name as the sole argument...
    SOPRA_Material = sopra_database("GaAs")

    # Can also load alpha data...
    GaAs_alpha = SOPRA_Material.load_alpha()

    out = GaAs_alpha[1][10]

    data = 163666134.03339368

    assert data == approx(out)
