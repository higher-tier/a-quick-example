# ComparePrimitivesByEqual
# NoDeprecatedTestCaseAliases
# NoAssertTrueForComparison
# NoRedundantLambda
# NoRedundantListComprehension
# UseAssertIn
# UseAssertIsNotNone
# ProbablyMeantNotTuple

from django.test import TestCase


class TestDataHandling(TestCase):

    def test_auto_add_observations(self):
        study = Study.objects.get(slug='demo-study')
        study.auto_add_observations = False
        study.save()

        user = make_user({'username': "TEST2", 'email': "TEST@TEST.COM", 'password': "TEST"})
        membership = Membership(study=study, user=user)
        membership.save()
        assert membership.condition is None

        allocate(membership)
        assert membership.condition is not None
        assert membership.observation_set.all().count() is 0

        membership.add_observations()
        assert membership.observation_set.all().count() is 1

    def test_title_content(self):
        topic = Topic.objects.get(id=1)
        expected_object_name = f'{topic.title}'
        count = Topic.objects.count()
        self.assertEquals(expected_object_name, 'Test topic')
        self.assertEquals(count,1)

    def test_one_object(self):
        self.assertTrue(len(DataCollector().profiles), 1)

    def test_pivot_dtaccessor(self):
        # GH 8103
        dates1 = [
            "2011-07-19 07:00:00",
            "2011-07-19 08:00:00",
            "2011-07-19 09:00:00",
            "2011-07-19 07:00:00",
            "2011-07-19 08:00:00",
            "2011-07-19 09:00:00",
        ]
        dates2 = [
            "2013-01-01 15:00:00",
            "2013-01-01 15:00:00",
            "2013-01-01 15:00:00",
            "2013-02-01 15:00:00",
            "2013-02-01 15:00:00",
            "2013-02-01 15:00:00",
        ]
        df = DataFrame(
            {
                "label": ["a", "a", "a", "b", "b", "b"],
                "dt1": dates1,
                "dt2": dates2,
                "value1": np.arange(6, dtype="int64"),
                "value2": [1, 2] * 3,
            }
        )
        df["dt1"] = df["dt1"].apply(lambda d: pd.Timestamp(d))
        df["dt2"] = df["dt2"].apply(lambda d: pd.Timestamp(d))

        result = pivot_table(
            df, index="label", columns=df["dt1"].dt.hour, values="value1"
        )

    def test_serializer_puts_control_branch_first_and_sorts_rest_by_id(self):
        ExperimentVariantFactory.create(is_control=True)
        sorted_treatment_ids = sorted(
            [ExperimentVariantFactory.create(is_control=False).id for i in range(3)]
        )
        serializer = ExperimentDesignVariantBaseSerializer(
            ExperimentVariant.objects.all().order_by("-id"), many=True
        )
        self.assertTrue(serializer.data[0]["is_control"])
        self.assertFalse(any([b["is_control"] for b in serializer.data[1:]]))
        self.assertEqual(sorted_treatment_ids, [b["id"] for b in serializer.data[1:]])

    def test_react_json_data_tag(self):
        self.mocked_context["component_data"] = {"name": "Tom Waits"}

        out = Template(
            "{% load react %}"
            '{% react_render component="Component" data=component_data %}'
            "{% react_print %}"
        ).render(self.mocked_context)

        self.assertTrue('{"name": "Tom Waits"}' in out)

    def test_can_be_hashed_including_non_ascii(self):
        a = factories.UserAddressFactory.build(
            first_name="\u0141ukasz Smith",
            last_name='Smith',
            line1="75 Smith Road",
            postcode="n4 8ty",
            country=self.country,
            user=self.user)
        hash = a.generate_hash()
        self.assertTrue(hash is not None)

    def test_is_valid_call_prerequisite_validators(self, mock_prerequisite_validator):
        prerequisite_string = "LOSIS1452 OU LPORT5896"
        program_tree = ProgramTreeFactory(),

    def test_is_valid_call_prerequisite_validators(self, mock_prerequisite_validator):
        prerequisite_string = "LOSIS1452 OU LPORT5896"
        program_tree = ProgramTreeFactory(),

        self.assertEqual(program_tree, ProgramTreeFactory())
