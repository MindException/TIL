# AZ 900 요약 정리

## cloud Computing 장점
agility(민첩성)
- 애플리케이션을 신속하게 배포, 테스트 및 시작할 수 있다

geo-clustered sites(지리적 그룹화된 사이트)
- Read-only geo-redundant storage는 secondary location에서도 읽을 수  있다.

Scalability(확장성)
- 요구에 따라서 동적으로 제공이 가능하다.

## 나머지

CapEX와 OpEX  
* CapEX  
    * 인프라를 구축하려는 초기 투자비용을 뜻한다.
    * datacenter와 관련 있다.

* OpEX
    * 운영 비용이다. 따라서 대표적으로 __종량제(pay-as-you-go subscription)__ 가 있다.
    * 종량제이기 때문에 월별 사용료를 지불하게 해야한다.(마이그레이션 할 경우)

구독 지원 플랜
- Basic, standard, developer,  professional direct
- Basic은 용량이 10gb까지이다.

Azure 가용성 영역
- Azure) Azure datacenter 오류(가용성으로 지역당 3개의 가용성 영역이 존재한다.)
- 사용자) 최소 2개 이상의 지역에 가상머신을 생성한다.
- 가상머신에서 가용성에 영향을 줄 수 있는 서비스 오류 알림을 보기 위한 Azure Portal은 가상머신에서 확인이 가능하다. (이건 Monitor가 아니다.)
- 99.99%의 가용성을 하기 위해서는 2개의 VM과 2개의 가용성 지역이 필요하다.
- datacenter 오류 발생 시 리소스 그룹이 같더라도 센터가 같아서 문제가 발생할 수 있다. 따라서 다른 datacenter에 저장해야 한다.
- 가용성 영역은 Azure 지역의 고유한 물리적 위치이다.
- 가용성 영역은 linux를 지원한다.
- 가용성 영역은 datacenter의 실패는 보장하지만 region의 실패는 보장하지 못한다.

Azure region(지역)
- 한 개의 지역 안에는 여러 개의 datacenter를 가지고 있다.
- 같은 지역 안에 데이터 전송은 무료이다.

Azure Policy(정책)
- 관리자가 해당지역에서만 리소스를 생성할 수 있는지 확인한다.
- 배포 중 리소스 속성 및 기존 리소스에 대한 요구 사항을 정의하는 데 사용할 수 있다.

신뢰 센터(trust center)
- 온 프레미스 환경에서 이전할 경우 지역 요구사항에 준수하는지 확인해야 한다.

Secrurity center
- just in time(JIT)

Scale
- Scale up은 데이터베이스 등에 메모리가 부족한 경우 더 키우는 것을 말하고
- Scale out은 웹서버가 부족할 경우 로드밸런싱을 위하여 웹서버를 추가하는 것을 말한다. 

Active Directory
- 네트워크 관리 도구로, 조직 내의 사용자, 그룹, 컴퓨터 등의 정보를 중앙에서 저장하고 관리한다.
- 사용자 계정을 이전(migration)할 때 사용한다.
- 테넌트를 사용하여 Azure potal에서 생성한다.

Azure Resource Manager templates vs management groups
* Azure Resource Manager templates은 자동으로 생성되는 리소스를 관리할 수 잇다.
* management groups는 구독권을 관리한다.

Azure DevTest Labs
* 많은 수의 가상머신을 같은 주에 생성하고 제거할 수 있다.
* 주로 가상머신 배포 예약을 한다.

VM과 VNet
- Azure 가상 네트워크(VNet)에 외부에서 접속하기 위해서는 P2S(Point-to-Site) VPN을 구성해야한다.
- Azure VM은 권한을 같은 리소스 그룹 내에 위임해야 동시에 가능하다.
- VNet의 이름은 구독 수준에서도 유니크해야한다.
- 격리 및 세분화
- 가상네트워크를 구축하기 위해서는 Gateway Subnet & VNet Gateway & VN 이 있어야한다
단 VM이 있을 경우 VN이 기본적으로 제공된다.

Azure ID 보호
- 보호와 관리를 혼용해서 출제하는데 관리는 없다.
- 로그인 위험 정책
- 사용자 위험 정책 - 식별되지 않은 IP에서 접속하면 암호 변경을 권장시킨다.

NSG(네트워크 보안 그룹)
- 웹서버와 데이터베이스를 연결할 수 있다.

Azure MFA
- 계획된 마이그레이션이 끝나면 사용자에게 끼치는 영향을 감소하기 위해 사용한다.

IaaS
- 사전 요구/서비스 및 응용 프로그램을 설치해야 하는 경우
- 소프트웨어 설치면 IaaS다 서비스가 SaaS이고
- 온-프레미스에서 사용하던 응용 프로그램이 있다면 그것 또한 IaaS로 마이그레이션 해야한다.

PaaS
- Azure) 가격 티어가 올라가면 추가 메모리를 제공한다.
- 아닐경우) 가격 티어가 올라가면 추가 메모리를 제공하지 않는다.
- Azure backup도 여기 포함
- 운영체제 관리를 최소화한다.

SaaS
- SaaS Solution을 구성해야 하며, 이것은 클라우드 공급자가 관리하고 책임진다.
- applicataion data
- 서버 운영체제와 대화식으로 한다.

fault tolerance(내결함성, 장애허용)
- 중지된 VM이 다시 작동이 가능한지 확인한다.

Disaster recovery
- 장애가 발생한 후 서비스를 복구하는 기능
- Azure Site Recovery에서 제공한다.

Dynamic scalability
- 서비스 부하가 높을 때 서비스에 컴퓨팅 리소스를 추가할 수 있는 기능

Latency(지연시간)
- 서비스가 요청에 응답하는 시간

public cloud
- datacenter를  사용하지 않는다.
- 종량제 가격
- 셀프 서비스 관리
- 퍼블릭 클라우드는 여러 기업이 클라우드 리소스의 일부를 각각 사용하는 __공유__ 개체이다.
- Guest users 뿐만이 아닌 Acitve Directory에 가입된 모든 사용자는 리소스에 접근이 가능하다.

hybrid cloud
- 하이브리드 클라우드는 온-프레미스 인프라(또는 프라이빗 클라우드)를 퍼블릭 클라우드와 결합하는 클라우드 컴퓨팅의 유형이다. 
- 하이브리드 클라우드를 사용하면 두 환경 간에 데이터와 앱을 이동할 수 있다.
- 하이브리드 클라우드를 생성하려면 리소스를 public 클라우드에 배포하여야 한다.

Azure Security Center
- JIT(Just-In-Time) 가상 머신(VM) 액세스 기능을 사용하여 Azure 가상 머신에 대한 인바운드 트래픽을 잠글 수 있다.
- regulatory requirements(규제 요구사항)이나 규제 리포트에 대해서 받을 수 있다.

elastic(신축성)
- 탄력성은 필요할 때 추가 컴퓨팅 리소스를 제공하고 필요하지 않을 때 컴퓨팅 리소스를 줄여 비용을 줄이는 기능이다.

채택(Adoption)
1. Define your strategy
2. Make a plan
3. Ready your organization
4. Adopt the cloud

Local Network gateways
- 온-프레미스 VPN 장치를 나타내는 Azure의 개체

Subscription
- 구독은 병합이 불가능하다.
- Azure 사용 시 제일 먼저 만들어야 하는 것
- 계정 관리자는 한 명만 가능하다.

새 지원 요청
- Azure 리소스에는 견적 제한이 있음으로 지원 요청을 열어 할당량 한도 증가를 요청할 수 있다.

가상 네트워크
- 가상 네트워크에는 여러 IP 주소 공간과 여러 서브넷이 있을 수 있다. Azure는 가상 네트워크 내의 서로 다른 서브넷 간에 트래픽을 자동으로 라우팅한다.

Archive access tier of Azure Storage
* 저장한 data를 읽거나 수정하려면 오프라인 상태에서 다시 온라인 계층으로 수화해야 한다.

LRS(LocallyRedundant Storage)
- 최소 3번의 데이터가 복제되어 저장된다.
- 기본적인 자동 백업 기능은 없다.
- 기본 500TB로 한도 용량이 크다.

Azure Service Health
- Microsoft가 Azure 구독에 배포된 리소스에 영향을 줄 수 있는 유지 관리를 수행할 계획일 때 알림

태그(tag)
- 상위 그룹에 태그를 걸었다고 해서 아래에도 적용되는 않는다
- 상위에 건 권한은 아래까지 내려간다

TCO
- 애저 돈계산은 여기서 한다.

Azure Monitor
- 가용성과 성능을 극대화하는 데 도움이 되며, 위험한 상황을 사전에 알리고 잠재적으로 조치를 취한다.
- Azure Log Analytics workspace로 경고를 보낸다.

Azure Advisior
- 백업되지 않은 VM을 표시하는 보고서 생성 기능
- 리소스 구성 및 사용량을 원격 분석한 후에 고사용성 및 보안을 개선하는데 도움이되는 해결 방안을 제시한다.

mapped drive
- File Service

AIP(Azure Information Protection)
- 문서(M365) 등을 검색, 분류 및 보호 기능

SLA(Service Level Agreement)
- 얼마나 가용성을 보장하여 줄 것인지 퍼센티지로 나타내는 것이다.
- 따라서 불확실한 공개 미리보기 리소스에 대한 것은 제외된다.

key vault
- 애저 키 자격 증명 모음
    1. 토큰, 암호, 인증, 비밀 액세스 기능
    2. 키관리 - 암호화 키
    3. 인증서 관리

firewall
- traffic 제한이 가능하다.

### 그 외
1. 서비스 종료 1년 전에 알림을 준다
2. Monthly Uptime % = (Maximum Available Minutes – Downtime) / Maximum Available Minutes X 100

web app from an iphone
1. Azure potal
2. cloud shell

window 10, ubuntu, mac os
1. Azure CLI
2. Azure potal
3. Azure powershell

130번 문제 까지


없는 문제 79번