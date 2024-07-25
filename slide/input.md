---
target: tasks
marp: true
theme: academic
math: katex
paginate: true

title: PolyLink Slide
subtitle: An Extensible Framework for Hierachical Dataflow Modeling
author: Dongho Park
date: 2024-07-19
---

<!-- _class: lead -->
<!-- _paginate: false -->

## PolyLink 


#### An Extensible Framework for Hierachical Dataflow Modeling

parkdongho28@naver.com
**Dongho Park**
**2024-07-19**

----
<!-- _header: Outline -->

[[toc]]

---
<!-- _class: chapter -->
<!-- _paginate: false -->

# **1. Spatial Accelerator**

---

<!-- _header: Key Metrics for Designing DNN Accelerators -->

**Throughput**: 
- The amount of work completed in a given period, typically measured in operations per second.

**IO Requirement**: 
- The amount and rate of data transfer needed in and out of the accelerator.

**Memory Requirement**: 
- The amount of memory needed to store data, weights, and intermediate results during computation.

**Workload Utilization**: 
- The efficiency with which the accelerator uses its computational resources.

**Latency**: 
- The time taken to complete a single operation or set of operations from start to finish.



---

<!-- _header: Dataflow Optimization -->

--- start-multi-column

![width:500px](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkJ34r%2FbtrbW2ernwv%2FRNx3WnjkxkELIHZSTZaXGk%2Fimg.png)

--- end-column ---


**(a) Weight Stationary (WS)**

- 가중치가 메모리 내에서 고정되어 있는 데이터 흐름 방법론으로, 활성화 값과 부분 합계가 이동
- 가중치의 이동을 최소화. 가중치가 계산 중 여러 번 재사용되기 때문에 유리

**(b) Output Stationary (OS)**

- 부분 합계(출력)가 메모리 내에서 고정되어 있는 데이터 흐름 방법론으로, 가중치와 활성화 값이 이동
- 부분 합의 이동을 최소화. 부분 합은 가중치와 활성화 값이 처리되는 동안 점진적으로 업데이트됩니다.

**(c) Input Stationary (IS)**

- 입력 활성화 값이 메모리 내에서 고정되어 있는 데이터 흐름 방법론으로, 가중치와 부분 합계가 이동
- 이 접근 방식은 입력 활성화 값의 이동을 최소화하여 한 번 로드된 입력 값이 여러 번 재사용

--- end-multi-column

---
<!-- _header: Dataflow Optimization(cont.) -->

![width:800px](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F0OlG9%2FbtrbVmYLGq9%2Fw5H6NqiyralSc65RlOPQ01%2Fimg.png)


**Row Stationary (RS)**

- 입력 행, 가중치 행 또는 출력 행의 데이터를 고정하여 사용하는 데이터 흐름 방법론입니다.
- 데이터의 특정 행을 로컬 메모리에 고정시키고, 다른 데이터는 처리 요소(PE) 사이를 이동시킵니다.
- 행 단위로 데이터를 고정함으로써 데이터 재사용을 극대화하고, 데이터 이동을 최소화할 수 있음
- [@eyeriss_jscc], [@eyeriss_isscc]



---
<!-- _header: HW Support for Flexibility -->


![width:800px](https://www.sigarch.org/wp-content/uploads/2023/06/Flexibility_Figure4-980x505.jpg)


- **(a)** 소프트 파티셔닝된 스크래치패드를 통한 타일링(T) 유연성으로, 각 텐서에 대한 공간을 동적으로 조정할 수 있음
- **(b)** 구성 가능한 주소 생성기를 통한 루프 순서(O) 유연성
- **(c)** PE(처리 요소)에서의 공간 및 시간 축 축소 지원을 통한 병렬화(P) 유연성
- **(d)** 동적 PE 그룹핑을 위한 유연한 네트워크 온 칩(NoC)을 통한 형태(S) 유연성


---
<!-- _class: chapter -->
<!-- _paginate: false -->

# **2. Architecture Modeling Framework**

---
<!-- _header: Key Concepts -->

**정확한 아키텍처 시뮬레이션**
- 다양한 workload(CONV2D, GEMM, etc)에 대하여 
- metric : **Throughput**, **IO Requirement**, **Memory Requirement**, **Workload Utilization**, **Latency**
- 아키텍처 설계(System Level Design) 단계에서 예측 

**optimal schedule를 탐색**
- tiling, skewing와 같은 optimization 테크닉을 적용 하였을 때 
- PPA를 개선하는 최적의 schdule을 탐색
- optimal한 아키텍처 탐색 시 architecutral design space exploaration이라 불림

**하드웨어 생성**
- 모델링한 아키텍처에 대하여 H/W IP에 대한 매핑
- verilog, chisel, c(hls) 코드를 생성

---
<!-- _header: Architecture 시뮬레이션을 위한 2가지 접근법 -->

**Brute-Force**
- 모든 iteration에 대하여 반복적으로 실행하여 hardware metric을 계산
- [@timeloop] 

**Formal Approach** 
- Integer Set Library를 활용
- 선형 제약 조건 으로 경계가 정해진 integer points의 Set과 Relation를 조작

---
<!-- _header: Schedule 탐색을 위한 3가지 접근법 -->

**Brute-force Approaches**
- 방법: 전체 탑색과 휴리스틱 결합.
- 기술: 지연 시간, 처리량, 전력 소비를 추정하기 위해 경량 분석 모델 사용.
- 단점: 복잡한 하드웨어에 대해 비용이 많이 들고 시간이 오래 걸림. 
- [@timeloop], [@dMazeRunner], [@triton], [@interstellar], [@marvel]

**Feedback-based Approaches**
- 방법: 머신러닝 또는 통계적 방법과 피드백 기반 모델 사용.
- 기술: 블랙박스(딥러닝) 또는 그라디언트 기반 탐색으로 스케줄링 공간 분포 학습.
- 단점: 광범위한 훈련 데이터 필요. 기존 하드웨어에 적합하지만 개발 중인 하드웨어에는 부적합.
- [@autotvm], [@halide], [@flexflow], [@gamma], [@mind-mapping]

**Constrained-optimization Approaches**
- 방법: 스케줄을 제약 최적화 문제로 공식화.
- 기술: 명령어 스케줄링, 고수준 합성, 메모리 분할, 알고리즘 선택 및 프로그램 합성에 널리 사용.
- 제한: 타일 크기 최적화 지원 부족으로 비 최적 스케줄 생성.
- [@pluto], [@autosa], [@tensor_comprehesion], [@tiramisu]


---
<!-- _class: chapter -->
<!-- _paginate: false -->

# 3. Polyhedral Model

---
<!-- _header: Key Concepts -->


**Iteration Domain (a.k.a Iteration Set)**
- Set of all possible loop iterations, represented as points in a multidimensional space.

**Access Function (a.k.a Access Map)**
- Describes how array elements are accessed within loops, mapping iterations to memory locations.

**Schedule (a.k.a Schedule Map)**
- Determines the execution order of iterations, mapping iterations to execution times.

**Dependence Relation (a.k.a Dependence Map)**
- Describes data dependencies between loop iterations, indicating how certain iterations depend on others.


----
<!-- _header: Analysis vs Schedule -->

**Polyhedral Analysis**
- Memory Requirement, 

**Schedule**



---
<!-- _class: chapter -->
<!-- _paginate: false -->

# 4. PolyLink Overview


---






---
<!-- _class: chapter -->
<!-- _paginate: false -->

# **Appendix**

---
<!-- _header: Bibliography -->

[bibliography]

