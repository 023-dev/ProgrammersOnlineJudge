# [level 2] 다음 큰 숫자 - 12911 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12911) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 70.0<br/>효율성: 30.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 04월 29일 23:57:47

### 문제 설명

<p data-sider-select-id="4e6c827b-102b-4f9e-93a7-2eb3a01092ae">자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.</p>

<ul>
<li data-sider-select-id="4f1ade84-76b1-4acd-a3a8-f04fc5e73eb0">조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.</li>
<li>조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.</li>
<li>조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.</li>
</ul>

<p>예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.</p>

<p>자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li>n은 1,000,000 이하의 자연수 입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td data-sider-select-id="e12b7cb8-35f5-48b3-bc6d-bd619448daba">78</td>
<td>83</td>
</tr>
<tr>
<td>15</td>
<td>23</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예#1<br>
문제 예시와 같습니다.<br>
입출력 예#2<br>
15(1111)의 다음 큰 숫자는 23(10111)입니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges