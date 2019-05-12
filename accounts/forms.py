from django import forms
from django.forms import RadioSelect


class Position(forms.Form):
    positions = (
        ('CF','CF'),
        ('ST','ST'),
        ('LWG','LWG'),
        ('RWG','RWG'),
        ('OMF','OMF'),
        ('RMF','RMF'),
        ('LMF','LMF'),
        ('CMF','CMF'),
        ('DMF','DMF'),
        ('LSB','LSB'),
        ('CB','CB'),
        ('RSB','RSB'),
        ('GK','GK')
    )
    positions = forms.ChoiceField(choices=positions, widget=RadioSelect)

class BasicStatus(forms.Form):
    min_val = 1
    max_val = 103
    req = True
    ofes = forms.IntegerField(
        label='OFE',
        min_value=min_val,
        max_value=max_val,
        required=req,

    )
    defs = forms.IntegerField(
        label='DEF',
        min_value=min_val,
        max_value=max_val,
        required=req,
    )
    pows = forms.IntegerField(
        label='POW',
        min_value=min_val,
        max_value=max_val,
        required=req,
    )
    spds = forms.IntegerField(
        label='SPD',
        min_value=min_val,
        max_value=max_val,
        required=req,
    )
    tecs = forms.IntegerField(
        label='TEC',
        min_value=min_val,
        max_value=max_val,
        required=req,
    )
    stas = forms.IntegerField(
        label='STA',
        min_value=min_val,
        max_value=max_val,
        required=req,
    )
    basic_statuses = (ofes, defs, pows, spds, tecs, stas)

class Speciality(forms.Form):
    specialities_dict = {
        "behind_1":"ビハインド◯", "behind_2":"ビハインド◎", "lead_1":"リード◯",
        "lead_2":"リード◎", "physical_1":"フィジカル◯", "physical_2":"フィジカル◎",
        "anti_inj_1":"ケガしにくさ◯", "anti_inj_2":"ケガしにくさ◎", "dash":"ダッシュ◯",
        "dribbler_1":"ドリブラー◯", "dribbler_2":"ドリブラー◎", "onetouch":"ワンタッチ◯",
        "trap_1":"トラップ◯", "trap_2":"トラップ◎", "air_1":"空中戦◯", "air_2":"空中戦◎",
        "bt_1":"突破力◯", "bt_2":"突破力◎", "kp_1":"キープ力◯", "kp_2":"キープ力◎",
        "pass_1":"パス◯", "pass_2":"パス◎", "tpass":"スルーパス◯", "cross":"クロス◯",
        "expansion":"展開力◯", "backspin":"バックスピン◯", "assist":"アシスト◯",
        "pass_intuition":"パス勘◯", "shoot_1":"シュート力◯", "shoot_2":"シュート力◎",
        "s_range":"シュートレンジ◯", "d_force_1":"決定力◯", "d_force_2":"決定力◎",
        "heading":"ヘディング◯", "mark":"マーク外し", "matchup":"マッチアップ◯",
        "st_ball_1":"ボール奪取◯", "st_ball_2":"ボール奪取◎", "covering":"カバーリング◯",
        "danger_sense":"危機察知◯", "def_reaction":"守備反応◯", "recapture":"奪還◯",
        "prefetch":"先読み", "coaching":"コーチング", "free_kick":"フリーキック◯",
        "pk":"PK◯", "long_throw":"ロングスロー", "teem_play":"チームプレー◯",
        "mood":"ムード◯", "f_split":"闘争心", "explo_pow":"爆発力◯", "guts_1":"根性◯",
        "guts_2":"根性◎", "recover_1":"回復◯", "recover_2":"回復◎", "hardwork":"ハードワーク◯",
        "playmaker":"司令塔", "captaincy":"キャプテンシー", "counter":"カウンター◯",
        "eos":"意外性", "vs_ace":"対エース◯", "fair_play":"フェアプレー",
        "malicia":"マリーシア", "big_match_1":"大一番◯", "big_match_2":"大一番◎",
        "first_goal":"ファーストゴール", "bench":"途中出場◯", "final_phase":"終盤◯",
        "lucky_boy":"ラッキーボーイ", "soccer_it_1":"サッカー脳◯", "soccer_it_2":"サッカー脳◎",
        "saving_1":"セービング◯", "saving_2":"セービング◎", "highball":"ハイボールキャッチ",
        "cocentration":"集中力", "low_punt_kick":"低弾道パントキック", "cor_avoid_1":"コーナー回避◯",
        "cor_avoid_2":"コーナー回避◎", "zero":"無失点", "vs_long_shoot":"対ロングシュート◯"
    }
    specialities_range = range(len(specialities_dict))



class SpecialitiesPoints(forms.Form):
    specialities_dict = [
        {"name":"ビハインド◯","tag":"behind_1","physical":"20","speed":"0","tecnic":"0","mental":"80","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"ビハインド◎","tag":"behind_2","physical":"30","speed":"0","tecnic":"0","mental":"120","cf":"0.4","wg":"0.4","st":"0.4","omf":"0.4","cmf":"0.4","smf":"0.4","dmf":"0.4","cb":"0.4","sb":"0.4","gk":"0.4",},
        {"name":"リード○","tag":"lead_1","physical":"55","speed":"45","tecnic":"0","mental":"0","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"リード◎","tag":"lead_2","physical":"83","speed":"68","tecnic":"0","mental":"0","cf":"0.4","wg":"0.4","st":"0.4","omf":"0.4","cmf":"0.4","smf":"0.4","dmf":"0.4","cb":"0.4","sb":"0.4","gk":"0.4",},
        {"name":"フィジカル◯","tag":"physical_1","physical":"120","speed":"23","tecnic":"8","mental":"0","cf":"1.4","wg":"1.4","st":"1.4","omf":"1.4","cmf":"1.4","smf":"1.4","dmf":"1.4","cb":"1.4","sb":"1.4","gk":"1.4",},
        {"name":"フィジカル◎","tag":"physical_2","physical":"160","speed":"30","tecnic":"10","mental":"0","cf":"0.6","wg":"0.6","st":"0.6","omf":"0.6","cmf":"0.6","smf":"0.6","dmf":"0.6","cb":"0.6","sb":"0.6","gk":"0.6",},
        {"name":"ケガしにくさ◯","tag":"anti_inj_1","physical":"105","speed":"0","tecnic":"0","mental":"45","cf":"1.4","wg":"1.4","st":"1.4","omf":"1.4","cmf":"1.4","smf":"1.4","dmf":"1.4","cb":"1.4","sb":"1.4","gk":"1.4",},
        {"name":"ケガしにくさ◎","tag":"anti_inj_2","physical":"140","speed":"0","tecnic":"0","mental":"60","cf":"0.6","wg":"0.6","st":"0.6","omf":"0.6","cmf":"0.6","smf":"0.6","dmf":"0.6","cb":"0.6","sb":"0.6","gk":"0.6",},
        {"name":"ダッシュ◯","tag":"dash","physical":"50","speed":"200","tecnic":"0","mental":"0","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"2","cb":"2","sb":"2","gk":"2",},
        {"name":"ドリブラー◯","tag":"dribbler_1","physical":"8","speed":"30","tecnic":"113","mental":"0","cf":"1.4","wg":"1.4","st":"1.4","omf":"1.4","cmf":"1.4","smf":"1.4","dmf":"1.4","cb":"1.4","sb":"1.4","gk":"1.4",},
        {"name":"ドリブラー◎","tag":"dribbler_2","physical":"10","speed":"40","tecnic":"150","mental":"0","cf":"0.6","wg":"0.6","st":"0.6","omf":"0.6","cmf":"0.6","smf":"0.6","dmf":"0.6","cb":"0.6","sb":"0.6","gk":"0.6",},
        {"name":"ワンタッチ◯","tag":"onetouch","physical":"0","speed":"40","tecnic":"160","mental":"0","cf":"3","wg":"3","st":"3","omf":"3","cmf":"3","smf":"3","dmf":"2","cb":"2","sb":"2","gk":"2",},
        {"name":"トラップ◯","tag":"trap_1","physical":"0","speed":"5","tecnic":"75","mental":"20","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"トラップ◎","tag":"trap_2","physical":"0","speed":"8","tecnic":"113","mental":"30","cf":"0.4","wg":"0.4","st":"0.4","omf":"0.4","cmf":"0.4","smf":"0.4","dmf":"0.4","cb":"0.4","sb":"0.4","gk":"0.4",},
        {"name":"空中戦◯","tag":"air_1","physical":"75","speed":"75","tecnic":"0","mental":"0","cf":"1.4","wg":"1.4","st":"1.4","omf":"1.4","cmf":"1.4","smf":"1.4","dmf":"1.4","cb":"1.4","sb":"1.4","gk":"1.4",},
        {"name":"空中戦◎","tag":"air_2","physical":"100","speed":"100","tecnic":"0","mental":"0","cf":"0.6","wg":"0.6","st":"0.6","omf":"0.6","cmf":"0.6","smf":"0.6","dmf":"0.6","cb":"0.6","sb":"0.6","gk":"0.6",},
        {"name":"突破力○","tag":"bt_1","physical":"8","speed":"15","tecnic":"128","mental":"0","cf":"1.4","wg":"1.4","st":"1.4","omf":"1.4","cmf":"1.4","smf":"1.4","dmf":"1","cb":"1","sb":"1.4","gk":"0",},
        {"name":"突破力◎","tag":"bt_2","physical":"10","speed":"20","tecnic":"170","mental":"0","cf":"0.6","wg":"0.6","st":"0.6","omf":"0.6","cmf":"0.6","smf":"0.6","dmf":"0","cb":"0","sb":"0.6","gk":"0",},
        {"name":"キープ力◯","tag":"kp_1","physical":"5","speed":"45","tecnic":"50","mental":"0","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"キープ力◎","tag":"kp_2","physical":"8","speed":"68","tecnic":"75","mental":"0","cf":"0.4","wg":"0.4","st":"0.4","omf":"0.4","cmf":"0.4","smf":"0.4","dmf":"0.4","cb":"0.4","sb":"0.4","gk":"0.4",},
        {"name":"パス◯","tag":"pass_1","physical":"10","speed":"0","tecnic":"70","mental":"20","cf":"1","wg":"1","st":"1","omf":"1.4","cmf":"1.4","smf":"1.4","dmf":"1.4","cb":"1","sb":"1","gk":"1",},
        {"name":"パス◎","tag":"pass_2","physical":"15","speed":"0","tecnic":"105","mental":"30","cf":"0.4","wg":"0.4","st":"0.4","omf":"0.6","cmf":"0.6","smf":"0.6","dmf":"0.6","cb":"0.4","sb":"0.4","gk":"0.4",},
        {"name":"スルーパス◯","tag":"tpass","physical":"10","speed":"0","tecnic":"110","mental":"80","cf":"2","wg":"2","st":"2","omf":"3","cmf":"3","smf":"3","dmf":"3","cb":"2","sb":"2","gk":"2",},
        {"name":"クロス◯","tag":"cross","physical":"20","speed":"20","tecnic":"140","mental":"20","cf":"2","wg":"3","st":"2","omf":"3","cmf":"3","smf":"3","dmf":"2","cb":"2","sb":"3","gk":"2",},
        {"name":"展開力◯","tag":"expansion","physical":"40","speed":"0","tecnic":"100","mental":"60","cf":"2","wg":"2","st":"2","omf":"3","cmf":"3","smf":"3","dmf":"3","cb":"2","sb":"2","gk":"2",},
        {"name":"バックスピン◯","tag":"backspin","physical":"0","speed":"3","tecnic":"51","mental":"10","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"アシスト◯","tag":"assist","physical":"0","speed":"10","tecnic":"80","mental":"110","cf":"2","wg":"2","st":"2","omf":"3","cmf":"3","smf":"3","dmf":"3","cb":"2","sb":"2","gk":"2",},
        {"name":"パス勘◯","tag":"pass_intuition","physical":"75","speed":"0","tecnic":"100","mental":"75","cf":"2","wg":"2","st":"2","omf":"3","cmf":"3","smf":"3","dmf":"3","cb":"3","sb":"3","gk":"3",},
        {"name":"シュート力◯","tag":"shoot_1","physical":"113","speed":"8","tecnic":"30","mental":"0","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"1.2","cb":"1.2","sb":"1.2","gk":"0",},
        {"name":"シュート力◎","tag":"shoot_2","physical":"150","speed":"10","tecnic":"40","mental":"0","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"0.8","cb":"0.8","sb":"0.8","gk":"0",},
        {"name":"シュートレンジ◯","tag":"s_range","physical":"138","speed":"25","tecnic":"63","mental":"25","cf":"3","wg":"3","st":"3","omf":"3","cmf":"3","smf":"3","dmf":"2","cb":"2","sb":"2","gk":"0",},
        {"name":"決定力◯","tag":"d_force_1","physical":"30","speed":"8","tecnic":"60","mental":"53","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"1.2","cb":"1.2","sb":"1.2","gk":"0",},
        {"name":"決定力◎","tag":"d_force_2","physical":"40","speed":"10","tecnic":"80","mental":"70","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"0.8","cb":"0.8","sb":"0.8","gk":"0",},
        {"name":"ヘディング◯","tag":"heading","physical":"50","speed":"100","tecnic":"50","mental":"0","cf":"3","wg":"3","st":"3","omf":"3","cmf":"2","smf":"2","dmf":"2","cb":"3","sb":"2","gk":"0",},
        {"name":"マーク外し","tag":"mark","physical":"19","speed":"88","tecnic":"0","mental":"19","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"1","cb":"1","sb":"1","gk":"0",},
        {"name":"マッチアップ◯","tag":"matchup","physical":"80","speed":"80","tecnic":"0","mental":"40","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"2","cb":"2","sb":"2","gk":"0",},
        {"name":"ボール奪取◯","tag":"st_ball_1","physical":"5","speed":"70","tecnic":"15","mental":"10","cf":"1","wg":"1","st":"1","omf":"1","cmf":"2","smf":"1","dmf":"2","cb":"2","sb":"2","gk":"0",},
        {"name":"ボール奪取◎","tag":"st_ball_2","physical":"8","speed":"105","tecnic":"23","mental":"15","cf":"0.4","wg":"0.4","st":"0.4","omf":"0.4","cmf":"1","smf":"0.4","dmf":"1","cb":"1","sb":"1","gk":"0",},
        {"name":"カバーリング◯","tag":"covering","physical":"0","speed":"25","tecnic":"25","mental":"75","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"危機察知◯","tag":"danger_sense","physical":"113","speed":"125","tecnic":"0","mental":"13","cf":"2","wg":"2","st":"2","omf":"2","cmf":"3","smf":"3","dmf":"3","cb":"3","sb":"3","gk":"3",},
        {"name":"守備反応◯","tag":"def_reaction","physical":"115","speed":"115","tecnic":"10","mental":"10","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"2","cb":"2","sb":"2","gk":"2",},
        {"name":"奪還◯","tag":"recapture","physical":"88","speed":"125","tecnic":"0","mental":"38","cf":"2","wg":"2","st":"2","omf":"3","cmf":"3","smf":"3","dmf":"3","cb":"3","sb":"3","gk":"2",},
        {"name":"先読み","tag":"prefetch","physical":"0","speed":"75","tecnic":"0","mental":"75","cf":"1","wg":"1","st":"1","omf":"1","cmf":"2","smf":"1","dmf":"2","cb":"2","sb":"2","gk":"0",},
        {"name":"コーチング","tag":"coaching","physical":"0","speed":"0","tecnic":"63","mental":"188","cf":"0.2","wg":"0.2","st":"0.2","omf":"0.2","cmf":"0.2","smf":"0.2","dmf":"3","cb":"3","sb":"3","gk":"3",},
        {"name":"フリーキック◯","tag":"free_kick","physical":"10","speed":"10","tecnic":"100","mental":"80","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"2","cb":"2","sb":"2","gk":"2",},
        {"name":"PK◯","tag":"pk","physical":"13","speed":"13","tecnic":"38","mental":"63","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"ロングスロー","tag":"long_throw","physical":"26","speed":"26","tecnic":"13","mental":"0","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"チームプレー◯","tag":"teem_play","physical":"0","speed":"0","tecnic":"15","mental":"135","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"ムード◯","tag":"mood","physical":"0","speed":"26","tecnic":"0","mental":"38","cf":"0.2","wg":"0.2","st":"0.2","omf":"0.2","cmf":"0.2","smf":"0.2","dmf":"0.2","cb":"0.2","sb":"0.2","gk":"0.2",},
        {"name":"闘争心","tag":"f_split","physical":"20","speed":"0","tecnic":"0","mental":"180","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"2","cb":"2","sb":"2","gk":"2",},
        {"name":"爆発力◯","tag":"explo_pow","physical":"40","speed":"40","tecnic":"0","mental":"120","cf":"3","wg":"3","st":"3","omf":"3","cmf":"3","smf":"3","dmf":"2","cb":"2","sb":"2","gk":"0",},
        {"name":"根性◯","tag":"guts_1","physical":"23","speed":"0","tecnic":"0","mental":"128","cf":"1.4","wg":"1.4","st":"1.4","omf":"1.4","cmf":"1.4","smf":"1.4","dmf":"1.4","cb":"1.4","sb":"1.4","gk":"1.4",},
        {"name":"根性◎","tag":"guts_2","physical":"30","speed":"0","tecnic":"0","mental":"170","cf":"0.6","wg":"0.6","st":"0.6","omf":"0.6","cmf":"0.6","smf":"0.6","dmf":"0.6","cb":"0.6","sb":"0.6","gk":"0.6",},
        {"name":"回復◯","tag":"recover_1","physical":"45","speed":"38","tecnic":"0","mental":"68","cf":"1.4","wg":"1.4","st":"1.4","omf":"1.4","cmf":"1.4","smf":"1.4","dmf":"1.4","cb":"1.4","sb":"1.4","gk":"1.4",},
        {"name":"回復◎","tag":"recover_2","physical":"60","speed":"50","tecnic":"0","mental":"90","cf":"0.6","wg":"0.6","st":"0.6","omf":"0.6","cmf":"0.6","smf":"0.6","dmf":"0.6","cb":"0.6","sb":"0.6","gk":"0.6",},
        {"name":"ハードワーク◯","tag":"hardwork","physical":"88","speed":"36","tecnic":"0","mental":"125","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"2","cb":"2","sb":"2","gk":"2",},
        {"name":"司令塔","tag":"playmaker","physical":"0","speed":"0","tecnic":"120","mental":"80","cf":"2","wg":"2","st":"2","omf":"3","cmf":"3","smf":"3","dmf":"3","cb":"2","sb":"2","gk":"2",},
        {"name":"キャプテンシー","tag":"captaincy","physical":"15","speed":"15","tecnic":"15","mental":"105","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"カウンター◯","tag":"counter","physical":"0","speed":"120","tecnic":"20","mental":"60","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"3","cb":"3","sb":"3","gk":"3",},
        {"name":"意外性","tag":"eos","physical":"50","speed":"0","tecnic":"25","mental":"50","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"対エース◯","tag":"vs_ace","physical":"40","speed":"80","tecnic":"0","mental":"80","cf":"2","wg":"2","st":"2","omf":"2","cmf":"2","smf":"2","dmf":"2","cb":"2","sb":"2","gk":"2",},
        {"name":"フェアプレー","tag":"fair_play","physical":"0","speed":"0","tecnic":"26","mental":"38","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"マリーシア","tag":"malicia","physical":"0","speed":"0","tecnic":"38","mental":"26","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"後半偏重","tag":"last_half","physical":"15","speed":"15","tecnic":"0","mental":"20","cf":"0.2","wg":"0.2","st":"0.2","omf":"0.2","cmf":"0.2","smf":"0.2","dmf":"0.2","cb":"0.2","sb":"0.2","gk":"0.2",},
        {"name":"大一番◯","tag":"big_match_1","physical":"8","speed":"8","tecnic":"8","mental":"28","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"大一番◎","tag":"big_match_2","physical":"11","speed":"11","tecnic":"11","mental":"41","cf":"0.4","wg":"0.4","st":"0.4","omf":"0.4","cmf":"0.4","smf":"0.4","dmf":"0.4","cb":"0.4","sb":"0.4","gk":"0.4",},
        {"name":"ファーストゴール","tag":"first_goal","physical":"10","speed":"160","tecnic":"0","mental":"30","cf":"3","wg":"3","st":"3","omf":"3","cmf":"3","smf":"3","dmf":"2","cb":"2","sb":"2","gk":"2",},
        {"name":"途中出場◯","tag":"bench","physical":"0","speed":"45","tecnic":"0","mental":"19","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"終盤◯","tag":"final_phase","physical":"38","speed":"13","tecnic":"13","mental":"63","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"ラッキーボーイ","tag":"lucky_boy","physical":"0","speed":"0","tecnic":"38","mental":"88","cf":"1","wg":"1","st":"1","omf":"1","cmf":"1","smf":"1","dmf":"1","cb":"1","sb":"1","gk":"1",},
        {"name":"サッカー脳◯","tag":"soccer_br_1","physical":"999","speed":"75","tecnic":"30","mental":"0","cf":"1.4","wg":"1.4","st":"1.4","omf":"1.4","cmf":"1.4","smf":"1.4","dmf":"1.4","cb":"1.4","sb":"1.4","gk":"1.4",},
        {"name":"サッカー脳◎","tag":"soccer_br_2","physical":"999","speed":"100","tecnic":"40","mental":"0","cf":"0.6","wg":"0.6","st":"0.6","omf":"0.6","cmf":"0.6","smf":"0.6","dmf":"0.6","cb":"0.6","sb":"0.6","gk":"0.6",},
        {"name":"セービング◯","tag":"saving_1","physical":"45","speed":"75","tecnic":"30","mental":"0","cf":"0","wg":"0","st":"0","omf":"0","cmf":"0","smf":"0","dmf":"0","cb":"0","sb":"0","gk":"2",},
        {"name":"セービング◎","tag":"saving_2","physical":"60","speed":"100","tecnic":"40","mental":"0","cf":"0","wg":"0","st":"0","omf":"0","cmf":"0","smf":"0","dmf":"0","cb":"0","sb":"0","gk":"1",},
        {"name":"ハイボールキャッチ","tag":"highball","physical":"30","speed":"75","tecnic":"30","mental":"15","cf":"0","wg":"0","st":"0","omf":"0","cmf":"0","smf":"0","dmf":"0","cb":"0","sb":"0","gk":"2",},
        {"name":"集中力","tag":"cocentration","physical":"0","speed":"25","tecnic":"75","mental":"150","cf":"0","wg":"0","st":"0","omf":"0","cmf":"0","smf":"0","dmf":"0","cb":"0","sb":"0","gk":"2",},
        {"name":"低弾道パントキック","tag":"low_punt_kick","physical":"70","speed":"30","tecnic":"100","mental":"0","cf":"0","wg":"0","st":"0","omf":"0","cmf":"0","smf":"0","dmf":"0","cb":"0","sb":"0","gk":"3",},
        {"name":"コーナー回避◯","tag":"cor_avoid_1","physical":"30","speed":"15","tecnic":"105","mental":"0","cf":"0","wg":"0","st":"0","omf":"0","cmf":"0","smf":"0","dmf":"0","cb":"0","sb":"0","gk":"2",},
        {"name":"コーナー回避◎","tag":"cor_avoid_2","physical":"40","speed":"20","tecnic":"140","mental":"0","cf":"0","wg":"0","st":"0","omf":"0","cmf":"0","smf":"0","dmf":"0","cb":"0","sb":"0","gk":"1",},
        {"name":"無失点","tag":"zero","physical":"75","speed":"0","tecnic":"0","mental":"75","cf":"0","wg":"0","st":"0","omf":"0","cmf":"0","smf":"0","dmf":"0","cb":"0","sb":"0","gk":"2",},
        {"name":"対ロングシュート◯","tag":"vs_long_shoot","physical":"0","speed":"90","tecnic":"20","mental":"90","cf":"0","wg":"0","st":"0","omf":"0","cmf":"0","smf":"0","dmf":"0","cb":"0","sb":"0","gk":"2",},
        ]
