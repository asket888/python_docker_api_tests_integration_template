class TestSuite {
    // Task 1
    function TestSum() {
        // write as many tests of regular /add endpoint as you think are necessary
        a = 1
        b = 2
        authorizedSummerClient.getSum(a, b).Returns(200, "{'result': 3}")
    }

    // Task 2
    function TestSumLazy() {
        a = 1
        b = 2
        authorizedSummerClient.getLazySum(a, b).atMostIn(timeout).Returns(200, "{'result': 3}")
    }

    // Task 3
    function TestSumRateLimit() {
        a = 1
        b = 2
        authorizedSummerClient.getLimitSum(a, b).times(2).Returns(200, "{'result': 3}").Returns(429, "{'error': 'Too Many Requests'}")
    }
}