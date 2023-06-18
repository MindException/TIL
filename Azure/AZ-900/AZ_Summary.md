# AZ 900 요약 정리

geo-clustered sites(지리적 그룹화된 사이트)
- Read-only geo-redundant storage는 secondary location에서도 읽을 수  있다.

CapEX와 OpEX  
* CapEX  
    * 인프라를 구축하려는 초기 투자비용을 뜻한다.

* OpEX
    * 운영 비용이다. 따라서 대표적으로 __종량제(pay-as-you-go subscription)__ 가 있다.

구독 지원 플랜
- Basic, standard, developer,  professional direct
- Basic은 용량이 10gb까지이다.

Azure 가용성 영역
- Azure) Azure datacenter 오류(가용성으로 지역당 3개의 가용성 영역이 존재한다.)
- 사용자) 최소 2개 이상의 지역에 가상머신을 생성한다.
- 가상머신에서 가용성에 영향을 줄 수 있는 서비스 오류 알림을 보기 위한 Azure Portal은 가상머신에서 확인이 가능하다. (이건 Monitor가 아니다.)
- 99.99%의 가용성을 하기 위해서는 2개의 VM과 2개의 가용성 지역이 필요하다.

Azure Policy(정책)
- 관리자가 해당지역에서만 리소스를 생성할 수 있는지 확인한다.

신뢰 센터(trust center)
- 온 프레미스 환경에서 이전할 경우 지역 요구사항에 준수하는지 확인해야 한다.

Scale
- Scale up은 데이터베이스 등에 메모리가 부족한 경우 더 키우는 것을 말하고
- Scale out은 웹서버가 부족할 경우 로드밸런싱을 위하여 웹서버를 추가하는 것을 말한다. 

Active Directory
- 네트워크 관리 도구로, 조직 내의 사용자, 그룹, 컴퓨터 등의 정보를 중앙에서 저장하고 관리한다.
- 사용자 계정을 이전(migration)할 때 사용한다.

Azure Resource Manager templates vs management groups
* Azure Resource Manager templates은 자동으로 생성되는 리소스를 관리할 수 잇다.
* management groups는 구독권을 관리한다.

Azure DevTest Labs
* 많은 수의 가상머신을 같은 주에 생성하고 제거할 수 있다.
* 주로 가상머신 배포 예약을 한다.

VM과 VNet
- Azure 가상 네트워크(VNet)에 외부에서 접속하기 위해서는 P2S(Point-to-Site) VPN을 구성해야한다.

Azure ID 보호
- 보호와 관리를 혼용해서 출제하는데 관리는 없다.
- 로그인 위험 정책
- 사용자 위험 정책 - 식별되지 않은 IP에서 접속하면 암호 변경을 권장시킨다.

NSG(네트워크 보안 그룹)
- 웹서버와 데이터베이스를 연결할 수 있다.

Azure MFA
- 계획된 마이그레이션이 끝나면 사용자에게 끼치는 영향을 감소하기 위해 사용한다.

SaaS
- SaaS Solution을 구성해야 하며, 이것은 클라우드 공급자가 관리하고 책임진다.

fault tolerance(내결함성)
- 중지된 VM이 다시 작동이 가능한지 확인한다.

public cloud
- datacenter를  사용하지 않으며, 

38번 문제 까지