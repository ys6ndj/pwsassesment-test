from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.forms import Position, BasicStatus, Speciality, SpecialitiesPoints
import pulp
# Create your views here.

@login_required
def index(request):
    return render(request, 'accounts/top.html')
def liner(position, sp_points, points):
    len_sp_points = len(sp_points)
    prob = pulp.LpProblem('selection problem', pulp.LpMaximize)
    #print(prob)
    x = [
        pulp.LpVariable('x[{}]'.format(i), 0, 1, 'Integer') for i in range(len_sp_points)
    ]

    obj = 0
    for i, sp in enumerate(sp_points):
        obj += sp[position] * x[i]
    prob += obj
    #print(prob)
    phy, spd, tec, men = 0, 0, 0, 0
    for i, sp in enumerate(sp_points):
        phy += sp["physical"] * x[i]
        spd += sp["speed"] * x[i]
        tec += sp["tecnic"] * x[i]
        men += sp["mental"] * x[i]
    """999 は最大値"""
    prob += (phy <= points[0])
    prob += (spd <= points[1])
    prob += (tec <= points[2])
    prob += (men <= points[3])

    #print(prob)

    status = prob.solve()
    print('Status', pulp.LpStatus[status])

    total = 0
    getable_sp_lst = []
    for i, sp in enumerate(sp_points):
        cnt = int(pulp.value(x[i]))
        if cnt > 0:
            getable_sp_lst.append([sp,cnt,sp[position]])
        total += sp[position] * cnt

    print('total', total)

    return total, getable_sp_lst

def hello_get_query(request):
    specialities = Speciality()
    sp_dict = specialities.specialities_dict
    sp_instance = SpecialitiesPoints()
    sp_points = sp_instance.specialities_dict
    """ポジションを取得"""
    position = request.GET.get('posision')
    """経験点を取得"""
    try:
        points = [
            int(request.GET.get('physical')),
            int(request.GET.get('speed')),
            int(request.GET.get('tecnic')),
            int(request.GET.get('mental'))
        ]
    except:
        points = [
            0, 0, 0, 0
        ]
    """特殊能力のコツレベルを取得"""
    got_sp_dict = {}
    no_get_sp_dict = {}
    for sp in sp_points:
        sp_name = sp['tag']
        try:
            #コツレベルの取得
            lv = int(request.GET.get(sp_name))
            sp['lv'] = lv
        except:
            break
    """取得済みの特殊能力の査定合計を計算"""
    sp_sum = 0
    no_got = []
    #コツレベル：割引率
    lv_lst = {0:1, 1:0.7, 2:0.5, 3:0.4, 4:0.3, 5:0.2}

    for sp in sp_points:
        try:
            sp[position] = float(sp[position])
            if sp['lv'] == 6:
                sp_sum += sp[position]
            else:
                lv = lv_lst[sp['lv']]
                sp['physical'] = int(float(sp['physical']) * lv)
                sp['speed'] = int(float(sp['speed']) * lv)
                sp['tecnic'] = int(float(sp['tecnic']) * lv)
                sp['mental'] = int(float(sp['mental']) * lv)
                no_got.append(sp)
        except:
            break
    try:
        total_assesment, getable_sp_lst = liner(position, no_got, points)
    except:
        total_assesment = 0
        getable_sp_lst = []
    d = {
        'positions': Position(),
        'basic_statuses': BasicStatus(),
        'specialities': specialities,
        'position': request.GET.get('posision'),
        'ofe': request.GET.get('ofe'),
        'def': request.GET.get('def'),
        'pow': request.GET.get('pow'),
        'spd': request.GET.get('spd'),
        'tec': request.GET.get('tec'),
        'sta': request.GET.get('sta'),
        'points': points,
        'no': no_got,
        't': sp_points,
        'sum':sp_sum,
        'total': total_assesment,
        'getable_sp_lst': getable_sp_lst,


    }

    return render(request, 'assesment.html', d)
